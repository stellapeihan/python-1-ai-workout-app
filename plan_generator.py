"""Rule-based workout plan generator for the MVP.

This module intentionally uses conservative, reviewed-template logic.
It does not diagnose injuries, does not promise outcomes, and does not
assume a user's one-rep max.
"""

from __future__ import annotations

from dataclasses import dataclass


GOAL_LABELS = {
    "muscle_gain": "增肌",
    "strength": "提升肌力",
    "cardio": "提升心肺",
    "general_fitness": "一般體能",
    "habit": "建立運動習慣",
}

EXPERIENCE_LABELS = {
    "beginner": "新手",
    "experienced": "具經驗",
    "returning": "回歸訓練",
}


@dataclass
class PlanInput:
    goal: str
    experience: str
    days_per_week: int
    minutes_per_session: int
    location: str
    equipment: list[str]
    preferences: str
    limitations: str
    review_period: str


def _base_exercises(equipment: list[str]) -> list[dict]:
    has_dumbbell = "dumbbell" in equipment
    has_leg_press = "leg_press" in equipment
    has_lat_pulldown = "lat_pulldown" in equipment
    has_bodyweight = "bodyweight" in equipment or not equipment

    exercises = []
    if has_dumbbell:
        exercises.append({
            "name": "啞鈴弓箭步蹲",
            "equipment_id": "dumbbell",
            "muscle_group": "下肢、臀部、核心",
            "sets": 2,
            "reps_or_time": "8-10 次/側",
            "rest": "60-90 秒",
            "demo_link": "/equipment/dumbbell",
            "load_principle": "選擇能維持正確動作、完成後仍保有 2-3 次餘裕的重量；不假設最大肌力。",
            "alternative": "徒手弓箭步蹲（無啞鈴或需要降低負荷時）",
        })
    elif has_bodyweight:
        exercises.append({
            "name": "徒手弓箭步蹲",
            "equipment_id": "dumbbell",
            "muscle_group": "下肢、臀部、核心",
            "sets": 2,
            "reps_or_time": "8-10 次/側",
            "rest": "60 秒",
            "demo_link": "/equipment/dumbbell",
            "load_principle": "以徒手控制動作品質為優先，保留 2-3 次餘裕。",
            "alternative": "縮短步幅的分腿蹲（平衡不足時）",
        })

    if has_leg_press:
        exercises.append({
            "name": "腿推機",
            "equipment_id": "leg_press",
            "muscle_group": "股四頭肌、臀部",
            "sets": 2,
            "reps_or_time": "10-12 次",
            "rest": "90 秒",
            "demo_link": "/equipment/leg_press",
            "load_principle": "選擇能全程控制、下背不離開背墊、仍保有 2-3 次餘裕的重量。",
            "alternative": "徒手深蹲（器材不可用時）",
        })
    else:
        exercises.append({
            "name": "徒手深蹲",
            "equipment_id": "leg_press",
            "muscle_group": "下肢、臀部",
            "sets": 2,
            "reps_or_time": "10-12 次",
            "rest": "60 秒",
            "demo_link": "/equipment/leg_press",
            "load_principle": "先以可控制的活動範圍完成，保留 2-3 次餘裕。",
            "alternative": "坐到椅子再站起（需要更保守版本時）",
        })

    if has_lat_pulldown:
        exercises.append({
            "name": "滑輪下拉機",
            "equipment_id": "lat_pulldown",
            "muscle_group": "背部、二頭肌",
            "sets": 2,
            "reps_or_time": "8-12 次",
            "rest": "60-90 秒",
            "demo_link": "/equipment/lat_pulldown",
            "load_principle": "選擇能控制肩胛下沉、不後仰甩動、仍保有 2-3 次餘裕的重量。",
            "alternative": "彈力帶下拉（器材不可用或需降低負荷時）",
        })
    else:
        exercises.append({
            "name": "彈力帶下拉/毛巾下拉動作模式練習",
            "equipment_id": "lat_pulldown",
            "muscle_group": "背部、肩胛控制",
            "sets": 2,
            "reps_or_time": "10-12 次",
            "rest": "45-60 秒",
            "demo_link": "/equipment/lat_pulldown",
            "load_principle": "以輕阻力練習肩胛下沉與控制，保留 2-3 次餘裕。",
            "alternative": "坐姿划船機（校內有器材且可舒適操作時）",
        })

    return exercises


def _adjust_for_experience(exercises: list[dict], experience: str) -> list[dict]:
    adjusted = [dict(e) for e in exercises]
    if experience == "experienced":
        for e in adjusted:
            e["sets"] = min(e["sets"] + 1, 4)
    elif experience == "returning":
        for e in adjusted:
            e["reps_or_time"] = e["reps_or_time"].replace("12", "10")
            e["load_principle"] += " 回歸訓練者請以較保守重量重新建立動作品質。"
    return adjusted


def _adjust_for_goal(exercises: list[dict], goal: str, minutes: int) -> list[dict]:
    adjusted = [dict(e) for e in exercises]
    if goal == "strength":
        for e in adjusted:
            e["reps_or_time"] = "6-8 次" if "次" in e["reps_or_time"] else e["reps_or_time"]
            e["rest"] = "90-120 秒"
            e["load_principle"] += " 以可維持動作品質的重量為主，不追求最大重量。"
    elif goal == "muscle_gain":
        for e in adjusted:
            e["reps_or_time"] = "8-12 次" if "次" in e["reps_or_time"] else e["reps_or_time"]
    elif goal == "cardio":
        for e in adjusted:
            e["sets"] = 2
            e["rest"] = "30-45 秒"
            e["load_principle"] += " 優先維持呼吸與動作節奏，不以疼痛或喘到無法說話為目標。"
    elif goal == "habit":
        for e in adjusted:
            e["sets"] = 2
            e["rest"] = "60 秒"
            e["load_principle"] += " 目標是建立可持續習慣，完成比追求強度更重要。"
    if minutes <= 30:
        adjusted = adjusted[:2]
        for e in adjusted:
            e["sets"] = min(e["sets"], 2)
    return adjusted


def _warmup(minutes: int) -> list[str]:
    base = [
        "2-3 分鐘輕度活動（原地踏步或快走），提升身體溫度。",
        "關節動態活動：肩、髖、膝、踝各 5-8 次，動作緩慢不疼痛。",
        "用極輕重量或徒手做 1 組暖身動作，確認活動範圍舒適。",
    ]
    if minutes >= 45:
        base.append("可額外加入 2 分鐘輕度核心啟動，如死蟲或平板支撐的保守版本。")
    return base


def _cooldown() -> list[str]:
    return [
        "2-3 分鐘慢走或緩慢活動，讓心率逐漸下降。",
        "針對本次使用肌群做溫和伸展，每個動作 15-30 秒，不彈震。",
        "若有不適，記錄感受並在下次訓練前調整或尋求專業協助。",
    ]


def generate_plan(data: PlanInput) -> dict:
    exercises = _base_exercises(data.equipment)
    exercises = _adjust_for_experience(exercises, data.experience)
    exercises = _adjust_for_goal(exercises, data.goal, data.minutes_per_session)

    prefs = (data.preferences or "").lower()
    if prefs:
        filtered = [e for e in exercises if not any(p.strip() and p.strip().lower() in e["name"].lower() for p in data.preferences.split(","))]
        if filtered:
            exercises = filtered

    limitations_note = None
    if data.limitations and data.limitations.strip():
        limitations_note = (
            "你填寫了身體限制或不適提醒。此課表僅為一般訓練參考，不構成醫療建議；"
            "請優先選擇不引起疼痛的動作範圍，必要時諮詢合格專業人士。"
        )
        for e in exercises:
            e["load_principle"] += " 若有不適，請降低範圍/負荷或改替代動作。"

    days = max(1, min(data.days_per_week, 6))
    sessions = []
    for day in range(1, days + 1):
        sessions.append({
            "day": f"第 {day} 天",
            "focus": GOAL_LABELS.get(data.goal, "一般訓練"),
            "duration_minutes": data.minutes_per_session,
            "warmup": _warmup(data.minutes_per_session),
            "main": exercises,
            "cooldown": _cooldown(),
        })

    return {
        "goal": GOAL_LABELS.get(data.goal, data.goal),
        "experience": EXPERIENCE_LABELS.get(data.experience, data.experience),
        "days_per_week": days,
        "minutes_per_session": data.minutes_per_session,
        "location": data.location,
        "equipment": data.equipment,
        "limitations_note": limitations_note,
        "review_period": data.review_period,
        "sessions": sessions,
        "general_notes": [
            "重量選擇原則：能維持正確動作、仍保有 2-3 次餘裕，不假設最大肌力。",
            "漸進方式：連續兩次訓練都能穩定完成且無不適時，才考慮小幅增加次數或負荷。",
            "休息日安排：至少保留 1-2 天恢復；同肌群高強度訓練避免連續安排。",
            "本課表為一般訓練建議，不保證特定成果，也不構成醫療診斷或治療。",
        ],
        "stop_signals": [
            "運動中出現疼痛、暈眩、胸悶、噁心或異常不適，請立即停止。",
            "嚴重或持續症狀應尋求醫療協助。",
            "有傷病、懷孕、慢性病或特殊健康狀況者，調整訓練前應諮詢合格專業人士。",
        ],
    }


def suggest_adjustment(feedback: dict) -> dict:
    """Return conservative adjustment suggestions. User must confirm before applying."""
    difficulty = feedback.get("difficulty", "")
    completed = feedback.get("completed", "")
    time_change = feedback.get("time_change", "")
    equipment_change = feedback.get("equipment_change", "")
    discomfort = feedback.get("discomfort", "")

    suggestions = []
    require_confirm = True
    safety_first = False

    if discomfort and discomfort.strip():
        safety_first = True
        suggestions.append("你回報了不適或疼痛。請先停止引起不適的動作，必要時尋求合格專業人士協助；系統不提供診斷。")
        suggestions.append("可將該動作改為不引起疼痛的替代動作，或暫時移除，並保留較長休息。")

    if difficulty == "too_hard":
        suggestions.append("下次將每個動作減少 1 組，或將次數下修到可保留 2-3 次餘裕的範圍。")
        suggestions.append("若重量造成動作失控，改用較輕重量或徒手替代動作。")
    elif difficulty == "too_easy":
        suggestions.append("若連續兩次訓練都能穩定完成且無不適，可考慮每個動作增加 1-2 次，或僅小幅增加負荷。")
        suggestions.append("不要在單次回饋後大幅增加重量或組數。")
    elif difficulty == "just_right":
        suggestions.append("維持目前安排，持續觀察動作品質與恢復狀況。")

    if completed == "partial":
        suggestions.append("下次可保留相同動作，但縮短訓練量（例如減少 1 組）以提升可完成性。")
    elif completed == "no":
        suggestions.append("下次可先安排較短版本（20-30 分鐘）或減少動作數，重建訓練習慣。")

    if time_change == "less_time":
        suggestions.append("可改為 20-30 分鐘版本：保留暖身、2 個主要動作各 2 組、簡短收操。")
    if equipment_change == "no_equipment":
        suggestions.append("可將器械動作替換為徒手或低阻力替代動作，並維持保守負荷。")

    if not suggestions:
        suggestions.append("目前沒有需要調整的項目。可維持原課表並持續記錄感受。")

    return {
        "suggestions": suggestions,
        "require_confirm": require_confirm,
        "safety_first": safety_first,
        "disclaimer": "調整建議為一般訓練參考，需由你確認後才套用；不構成醫療建議，也不保證成果。",
    }
