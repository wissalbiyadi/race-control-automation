import os
import requests
import json
import time
import pandas as pd

# ✅ Correct relative path to mock data from this file's location
MOCK_PATH = os.path.join(os.path.dirname(__file__), '../data/mock_live_timing.json')


def load_mock_data(path=MOCK_PATH):
    """
    Load mock race data from local JSON file.
    Used as a fallback if live API is unreachable.
    """
    with open(path, 'r') as f:
        return json.load(f)


def load_live_data():
    """
    Fetch latest F1 session data from OpenF1 API.
    Returns data if valid, or None to trigger fallback.
    """
    url = "https://api.openf1.org/v1/sessions?session_key=latest"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and data:
            return data  # API returned a list of session objects
        return None

    except requests.RequestException as e:
        print(f"⚠️ Live API failed: {e}")
        return None


def simulate_live_feed(frames, delay=2):
    """
    Simulates a live feed by yielding frames one by one with a delay.
    Useful for testing UI behavior as if data were streaming in.
    """
    for frame in frames:
        yield frame
        time.sleep(delay)
