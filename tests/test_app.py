import importlib.util
from pathlib import Path

import requests


def load_app_module():
    app_path = Path(__file__).resolve().parents[1] / "app.py"
    spec = importlib.util.spec_from_file_location("gopal_app", app_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_check_ollama_running_handles_connection_errors(monkeypatch):
    app = load_app_module()

    def fake_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError("connection refused")

    monkeypatch.setattr(app.requests, "get", fake_get)

    assert app.check_ollama_running("http://localhost:11434") is False


def test_check_ollama_running_returns_true_for_healthy_server(monkeypatch):
    app = load_app_module()

    class DummyResponse:
        status_code = 200

    def fake_get(url, timeout=5):
        assert url == "http://localhost:11434/api/tags"
        return DummyResponse()

    monkeypatch.setattr(app.requests, "get", fake_get)

    assert app.check_ollama_running("http://localhost:11434") is True
