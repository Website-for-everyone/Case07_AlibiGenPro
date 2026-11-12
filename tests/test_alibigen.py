"""
Test Suite for AlibiGen Pro (Case 07)
Verifies:
1. Tri-axis excuse generation logic and believability scoring
2. Pillow fake crash screenshot synthesis for all 4 presets
3. FastAPI web routes (/health, /api/generate, /api/crash-image)
4. Bot router and inline query handler registration
"""
import pytest
from fastapi.testclient import TestClient

import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
for mod in list(sys.modules.keys()):
    if mod.startswith("api") or mod.startswith("bot"):
        sys.modules.pop(mod, None)
if str(PROJECT_ROOT) in sys.path:
    sys.path.remove(str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT))

from api.server import app, build_excuse, generate_crash_image
from bot.bot import dp

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["app"] == "AlibiGenPro"


def test_excuse_generator_algorithm():
    # Test high tech, low absurdity
    res = build_excuse("teamlead", absurdity=10, pity=20, tech=90)
    assert len(res["text"]) > 20
    assert res["believability"] >= 70
    assert res["recipient"] == "teamlead"

    # Test high absurdity, low tech
    res_absurd = build_excuse("client", absurdity=95, pity=30, tech=10)
    assert res_absurd["believability"] < 60
    assert "Здравствуйте" in res_absurd["text"] or "Добрый" in res_absurd["text"] or "Привет" in res_absurd["text"]


def test_api_generate_route():
    payload = {
        "recipient": "boss",
        "absurdity": 25,
        "pity": 35,
        "tech": 80
    }
    response = client.post("/api/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "text" in data
    assert 10 <= data["believability"] <= 99
    assert data["recipient"] == "boss"


def test_crash_image_generation():
    presets = ["bsod", "kernel_panic", "gateway500", "compiler"]
    for p in presets:
        img_bytes = generate_crash_image(p, "TEST_ERR_TRACE")
        assert len(img_bytes) > 500
        # PNG Magic Header
        assert img_bytes.startswith(b'\x89PNG\r\n\x1a\n')


def test_api_crash_image_endpoint():
    response = client.get("/api/crash-image?preset=bsod&error_detail=FATAL_0x01")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"
    assert len(response.content) > 500


def test_bot_dispatcher_and_handlers():
    assert dp is not None
    # Check that inline query handler is registered
    assert dp.inline_query.handlers is not None
    assert len(dp.inline_query.handlers) > 0
    # Check message handlers
    assert len(dp.message.handlers) >= 3
