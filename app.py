from flask import Flask, render_template, request, redirect, url_for, session

from equipment_data import EQUIPMENT, get_equipment_by_id, search_equipment
from plan_generator import PlanInput, generate_plan, suggest_adjustment

app = Flask(__name__)
app.secret_key = "dev-only-mvp-secret"


@app.context_processor
def inject_globals():
    return {
        "all_equipment": EQUIPMENT,
        "safety_banner": "若運動中出現疼痛、暈眩、胸悶或不適，請立即停止；嚴重或持續症狀應尋求醫療協助。",
    }


@app.get("/")
def index():
    query = request.args.get("q", "").strip()
    muscle = request.args.get("muscle", "").strip()
    results = search_equipment(query=query, muscle_group=muscle)
    muscles = sorted({m for item in EQUIPMENT for m in item["muscle_groups"]})
    return render_template("index.html", query=query, muscle=muscle, results=results, muscles=muscles)


@app.get("/equipment/<equipment_id>")
def equipment_detail(equipment_id: str):
    item = get_equipment_by_id(equipment_id)
    if not item:
        return render_template("not_found.html", message="找不到該器材。請回到搜尋頁確認名稱。"), 404
    return render_template("equipment.html", item=item)


@app.route("/identify", methods=["GET", "POST"])
def identify():
    """Low-risk photo assist: never auto-confirm an uncertain identification."""
    if request.method == "GET":
        return render_template("identify.html", suggestion=None, confidence=None, filename=None)

    file = request.files.get("photo")
    if not file or not file.filename:
        return render_template("identify.html", suggestion=None, confidence="none", filename=None, error="請選擇一張器材照片。")

    # MVP safe fallback: do not claim visual recognition. Ask user to confirm/search.
    filename = file.filename
    suggestion = None
    confidence = "low"
    lower = filename.lower()
    for item in EQUIPMENT:
        if item["id"] in lower or any(alias.lower() in lower for alias in item["aliases"]):
            suggestion = item
            confidence = "medium"
            break

    return render_template(
        "identify.html",
        suggestion=suggestion,
        confidence=confidence,
        filename=filename,
        error=None,
    )


@app.route("/plan", methods=["GET", "POST"])
def plan():
    if request.method == "GET":
        return render_template("plan_form.html", form={}, generated=None, feedback_result=None)

    form = request.form
    try:
        days = int(form.get("days_per_week", "2"))
        minutes = int(form.get("minutes_per_session", "30"))
    except ValueError:
        days, minutes = 2, 30
    days = max(1, min(days, 6))
    minutes = max(15, min(minutes, 120))

    equipment = form.getlist("equipment")
    data = PlanInput(
        goal=form.get("goal", "habit"),
        experience=form.get("experience", "beginner"),
        days_per_week=days,
        minutes_per_session=minutes,
        location=form.get("location", "中央大學校內健身房"),
        equipment=equipment,
        preferences=form.get("preferences", ""),
        limitations=form.get("limitations", ""),
        review_period=form.get("review_period", ""),
    )
    generated = generate_plan(data)
    session["last_plan"] = generated
    session["last_form"] = dict(form)
    session["last_form"]["equipment"] = equipment
    return render_template("plan_form.html", form=session["last_form"], generated=generated, feedback_result=None)


@app.post("/plan/feedback")
def plan_feedback():
    generated = session.get("last_plan")
    form = session.get("last_form", {})
    if not generated:
        return redirect(url_for("plan"))

    feedback = {
        "difficulty": request.form.get("difficulty", ""),
        "completed": request.form.get("completed", ""),
        "time_change": request.form.get("time_change", ""),
        "equipment_change": request.form.get("equipment_change", ""),
        "discomfort": request.form.get("discomfort", ""),
    }
    feedback_result = suggest_adjustment(feedback)
    return render_template("plan_form.html", form=form, generated=generated, feedback_result=feedback_result, feedback=feedback)


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(debug=True)
