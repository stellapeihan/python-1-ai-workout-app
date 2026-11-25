"""Reviewed equipment content for the NCU gym MVP demo.

Content status: sample/demo data only. All entries must be reviewed by qualified
professionals before production use.
"""

EQUIPMENT = [
    {
        "id": "dumbbell",
        "name": "啞鈴",
        "aliases": ["啞鈴", "dumbbell", "自由重量"],
        "muscle_groups": ["上肢", "胸", "肩", "背", "手臂", "核心"],
        "training_purposes": ["增肌", "提升肌力", "一般體能", "建立運動習慣"],
        "level": "新手可，在指導下使用",
        "location_note": "中央大學校內健身房自由重量區（示範資料，請以現場實際配置為準）",
        "pre_use_checks": [
            "確認啞鈴握把無裂損、鬆動或油污，避免滑手。",
            "確認重量標示清楚，選擇能維持正確動作且仍保有餘裕的重量。",
            "確認周圍有足夠空間，不會碰撞他人或器材。",
            "如有可調式啞鈴，確認卡扣或調整機構已固定。",
        ],
        "setup_steps": [
            "先從較輕重量開始，雙手或單手穩定握住握把中央。",
            "站姿時雙腳與肩同寬、膝蓋微彎、核心收穩。",
            "動作前確認手腕中立，不過度彎折。",
        ],
        "movement_steps": [
            "以啞鈴弓箭步蹲為例：雙手持啞鈴自然垂於身側。",
            "一步向前或向後踏出，前後腳膝蓋朝腳尖方向彎曲。",
            "下蹲至前腳大腿接近水平、後膝接近地面但不碰撞地面。",
            "吐氣時以前腳腳跟發力回到起始姿勢，吸氣下蹲、吐氣起身。",
        ],
        "breathing": "下放或用力準備時吸氣，發力回到起始位置時吐氣；避免憋氣硬撐。",
        "common_mistakes": [
            {"mistake": "重量過重導致聳肩或手腕翻折", "fix": "降低重量，保持肩膀下沉、手腕中立。"},
            {"mistake": "下蹲時前膝大幅內扣", "fix": "膝蓋方向對齊第二腳趾，控制速度。"},
            {"mistake": "身體晃動借力", "fix": "縮小動作幅度或減重，保持核心穩定。"},
        ],
        "safety_notes": [
            "若感到疼痛、暈眩、胸悶或不適，應立即停止訓練。",
            "避免在疲勞或動作失控時勉強完成次數。",
            "有傷病、懷孕、慢性病或特殊健康狀況者，開始或調整訓練前應諮詢合格專業人士。",
        ],
        "alternatives": [
            {"name": "徒手弓箭步蹲", "reason": "沒有啞鈴或想先練習平衡與動作模式時可使用。"},
            {"name": "高腳杯深蹲（Goblet Squat）", "reason": "若只有單一啞鈴，可用來練習下肢與核心穩定。"},
        ],
        "media": {
            "image": "/static/images/dumbbell.svg",
            "video": "",
            "text_alternative": "文字版：雙手持啞鈴於身側，前後腳站穩後下蹲，膝蓋朝腳尖方向，保持軀幹穩定，吐氣站起。",
        },
        "review": {
            "status": "示範草稿 - 尚未經專業審閱",
            "reviewer": "待具備相關資格人員審閱",
            "source": "示範內容，依一般健身房安全原則整理；正式上線前需校內器材盤點與專業審閱",
            "updated_at": "2026-11-25",
        },
    },
    {
        "id": "leg_press",
        "name": "腿推機",
        "aliases": ["腿推機", "leg press", "蹬腿機"],
        "muscle_groups": ["下肢", "股四頭肌", "臀部"],
        "training_purposes": ["增肌", "提升肌力", "一般體能"],
        "level": "新手可，在熟悉調整後使用",
        "location_note": "中央大學校內健身房下肢器械區（示範資料，請以現場實際配置為準）",
        "pre_use_checks": [
            "確認配重插銷完整插入指定重量片。",
            "確認座椅背墊、踏板與安全扣正常，無異音或鬆動。",
            "確認重量可讓你全程控制，不需用力憋氣或彈震。",
        ],
        "setup_steps": [
            "調整座椅，使臀部與下背貼合背墊，膝蓋彎曲時不過度擠壓胸口。",
            "雙腳踩在踏板中央，與髖同寬或略寬，腳尖自然朝前或微外開。",
            "握住把手穩定上半身，測試小幅度推動是否順暢。",
        ],
        "movement_steps": [
            "鬆開安全扣後，吸氣緩慢屈膝，讓踏板靠近但不讓下背離開背墊。",
            "膝蓋朝腳尖方向移動，避免內扣或過度鎖死。",
            "吐氣時腳跟穩定推回起始位置，膝蓋保留微彎，不完全鎖死。",
            "完成組數後先固定安全扣，再離開器材。",
        ],
        "breathing": "屈膝下放時吸氣，推起時吐氣；全程避免憋氣硬舉。",
        "common_mistakes": [
            {"mistake": "下放太深導致屁股離開座墊", "fix": "縮短下放距離，保持下背貼緊背墊。"},
            {"mistake": "推到頂端時膝蓋完全鎖死", "fix": "終點保留微彎，維持肌肉張力。"},
            {"mistake": "重量過重導致腳跟離開踏板", "fix": "降低重量，腳跟全程貼穩踏板。"},
        ],
        "safety_notes": [
            "若下背、膝蓋或髖部出現疼痛，立即停止並調整或改用替代動作。",
            "不要用手推膝蓋輔助完成動作。",
            "嚴重或持續症狀應尋求醫療協助；本內容不構成醫療建議。",
        ],
        "alternatives": [
            {"name": "徒手深蹲", "reason": "無腿推機或想練習基本下肢動作模式時可使用。"},
            {"name": "坐姿腿伸機/腿屈機組合", "reason": "若想降低整體負荷或分別訓練前後側大腿，可作為替代安排。"},
        ],
        "media": {
            "image": "/static/images/leg_press.svg",
            "video": "",
            "text_alternative": "文字版：背部貼緊座墊，雙腳踩踏板，屈膝下放時下背不離墊，吐氣推回並保留膝蓋微彎。",
        },
        "review": {
            "status": "示範草稿 - 尚未經專業審閱",
            "reviewer": "待具備相關資格人員審閱",
            "source": "示範內容，依一般健身房安全原則整理；正式上線前需校內器材盤點與專業審閱",
            "updated_at": "2026-11-25",
        },
    },
    {
        "id": "lat_pulldown",
        "name": "滑輪下拉機",
        "aliases": ["滑輪下拉機", "lat pulldown", "下拉機"],
        "muscle_groups": ["背部", "上肢", "二頭肌"],
        "training_purposes": ["增肌", "提升肌力", "一般體能"],
        "level": "新手可，在調整座椅與重量後使用",
        "location_note": "中央大學校內健身房上肢器械區（示範資料，請以現場實際配置為準）",
        "pre_use_checks": [
            "確認插銷固定、握把與鋼索無明顯磨損。",
            "確認大腿固定墊可穩定貼合，避免拉動時身體浮起。",
            "選擇能控制肩胛下沉與拉回的重量。",
        ],
        "setup_steps": [
            "調整座椅高度，使大腿固定墊貼緊大腿上方。",
            "坐穩後雙腳平放地面，握住握把略寬於肩。",
            "胸口微挺、肩膀下沉，避免聳肩。",
        ],
        "movement_steps": [
            "吸氣準備，先讓肩胛微下沉。",
            "吐氣時將握把拉向上胸附近，手肘朝下後方。",
            "停留一瞬感受背部出力，吸氣緩慢放回起始位置。",
            "全程控制速度，不讓配重片猛烈撞擊。",
        ],
        "breathing": "放回時吸氣，下拉時吐氣；避免聳肩或憋氣。",
        "common_mistakes": [
            {"mistake": "用身體後仰甩動重量", "fix": "減輕重量，軀幹保持穩定，只做肩胛與手臂控制的下拉。"},
            {"mistake": "拉到頸後", "fix": "改拉至上胸前方，減少肩頸壓力。"},
            {"mistake": "聳肩代償", "fix": "先做肩胛下沉，再啟動下拉。"},
        ],
        "safety_notes": [
            "肩頸若有不適，停止動作並改用較保守的替代動作。",
            "避免快速彈震或頸後下拉。",
            "若有傷病、疼痛或特殊健康狀況，應先諮詢合格專業人士。",
        ],
        "alternatives": [
            {"name": "彈力帶下拉", "reason": "器材不可用或想降低負荷時可使用。"},
            {"name": "坐姿划船機", "reason": "若目標是背部訓練，可改用划船動作模式並調整重量。"},
        ],
        "media": {
            "image": "/static/images/lat_pulldown.svg",
            "video": "",
            "text_alternative": "文字版：坐穩固定大腿，肩胛下沉後將握把拉至上胸，控制放回，不後仰甩動。",
        },
        "review": {
            "status": "示範草稿 - 尚未經專業審閱",
            "reviewer": "待具備相關資格人員審閱",
            "source": "示範內容，依一般健身房安全原則整理；正式上線前需校內器材盤點與專業審閱",
            "updated_at": "2026-11-25",
        },
    },
]


def get_equipment_by_id(equipment_id: str):
    return next((item for item in EQUIPMENT if item["id"] == equipment_id), None)


def search_equipment(query: str = "", muscle_group: str = ""):
    query = (query or "").strip().lower()
    muscle_group = (muscle_group or "").strip()
    results = []
    for item in EQUIPMENT:
        name_hit = not query or query in item["name"].lower() or any(query in alias.lower() for alias in item["aliases"])
        muscle_hit = not muscle_group or muscle_group in item["muscle_groups"]
        if name_hit and muscle_hit:
            results.append(item)
    return results
