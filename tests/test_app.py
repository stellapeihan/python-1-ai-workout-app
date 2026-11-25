import pytest

from app import app as flask_app
from plan_generator import PlanInput, generate_plan, suggest_adjustment


@pytest.fixture()
def client():
    flask_app.config.update(TESTING=True, SECRET_KEY="test-secret")
    with flask_app.test_client() as client:
        yield client


def test_index_shows_equipment(client):
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.get_data(as_text=True)
    assert "啞鈴" in body
    assert "腿推機" in body
    assert "滑輪下拉機" in body


def test_search_by_name(client):
    resp = client.get("/?q=啞鈴")
    body = resp.get_data(as_text=True)
    assert resp.status_code == 200
    assert "/equipment/dumbbell" in body
    assert "/equipment/leg_press" not in body
    assert "/equipment/lat_pulldown" not in body

def test_equipment_detail_has_safety_and_review(client):
    resp = client.get("/equipment/dumbbell")
    assert resp.status_code == 200
    body = resp.get_data(as_text=True)
    assert "審閱狀態" in body
    assert "示範草稿 - 尚未經專業審閱" in body
    assert "停止訓練" in body or "立即停止" in body
    assert "替代" in body


def test_equipment_not_found(client):
    resp = client.get("/equipment/unknown")
    assert resp.status_code == 404


def test_identify_get(client):
    resp = client.get("/identify")
    assert resp.status_code == 200
    assert "輔助辨識" in resp.get_data(as_text=True)


def test_identify_post_without_file(client):
    resp = client.post("/identify", data={})
    assert resp.status_code == 200
    assert "請選擇一張器材照片" in resp.get_data(as_text=True)


def test_plan_generation_route(client):
    resp = client.post("/plan", data={
        "goal": "habit",
        "experience": "beginner",
        "days_per_week": "2",
        "minutes_per_session": "30",
        "location": "中央大學校內健身房",
        "equipment": ["dumbbell", "bodyweight"],
        "preferences": "",
        "limitations": "",
        "review_period": "",
    })
    assert resp.status_code == 200
    body = resp.get_data(as_text=True)
    assert "你的基礎課表" in body
    assert "不保證特定成果" in body
    assert "立即停止" in body


def test_plan_generator_limitations_note():
    plan = generate_plan(PlanInput(
        goal="habit", experience="beginner", days_per_week=2,
        minutes_per_session=30, location="NCU", equipment=["bodyweight"],
        preferences="", limitations="膝蓋不適", review_period="",
    ))
    assert plan["limitations_note"] is not None
    assert "不構成醫療建議" in plan["limitations_note"]


def test_adjustment_is_conservative_and_requires_confirmation():
    result = suggest_adjustment({
        "difficulty": "too_easy",
        "completed": "yes",
        "time_change": "same",
        "equipment_change": "same",
        "discomfort": "",
    })
    assert result["require_confirm"] is True
    joined = "\n".join(result["suggestions"])
    assert "連續兩次" in joined
    assert "不要在單次回饋後大幅增加" in joined


def test_adjustment_discomfort_is_safety_first():
    result = suggest_adjustment({
        "difficulty": "too_hard",
        "completed": "partial",
        "time_change": "same",
        "equipment_change": "same",
        "discomfort": "肩膀痛",
    })
    assert result["safety_first"] is True
    assert any("停止" in s for s in result["suggestions"])
    assert any("不提供診斷" in s for s in result["suggestions"])
