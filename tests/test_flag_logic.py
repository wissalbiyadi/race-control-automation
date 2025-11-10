import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.flag_logic import detect_flag_changes

def test_detect_flag_changes():
    prev = {
        "time": "00:00",
        "sector_flags": {
            "sector_1": "green",
            "sector_2": "green",
            "sector_3": "green"
        }
    }

    curr = {
        "time": "00:10",
        "sector_flags": {
            "sector_1": "yellow",
            "sector_2": "green",
            "sector_3": "green"
        }
    }

    changes = detect_flag_changes(prev, curr)

    assert len(changes) == 1
    assert changes[0]["sector"] == "sector_1"
    assert changes[0]["from"] == "green"
    assert changes[0]["to"] == "yellow"
    assert changes[0]["time"] == "00:10"