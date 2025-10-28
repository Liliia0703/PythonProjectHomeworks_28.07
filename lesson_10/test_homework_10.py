import os
import time
import pytest
from lesson_10.homework_10 import log_event

LOG_PATH = os.path.join(os.path.dirname(__file__), "login_system.log")

@pytest.fixture(autouse=True)
def clean_log_file():
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)
    yield
    if os.path.exists(LOG_PATH):
        os.remove(LOG_PATH)

def wait_for_log(path, attempts=20, delay=0.1):
    for _ in range(attempts):
        if os.path.exists(path):
            return
        time.sleep(delay)
    raise FileNotFoundError(f"Файл логів не створився навіть після очікування: {path}")

def read_log() -> str:
    wait_for_log(LOG_PATH)
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        return f.read()

def test_log_success():
    log_event("Lilia", "success")
    text = read_log()
    assert "INFO" in text
    assert "Lilia" in text
    assert "success" in text

def test_log_expired():
    log_event("Lilia", "expired")
    text = read_log()
    assert "WARNING" in text
    assert "expired" in text

def test_log_failed():
    log_event("Lilia", "failed")
    text = read_log()
    assert "ERROR" in text
    assert "failed" in text