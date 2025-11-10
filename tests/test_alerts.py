import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.alerts import process_alerts

def test_yellow_flag_long_duration():
    flag_changes = [
        {
            "sector": "sector_1",
            "from": "yellow",
            "to": "green",
            "time": "00:45"
        }
    ]

    # Simulate previous yellow flag started at 00:10
    from src.alerts import active_flags
    active_flags["sector_1"] = {
        "flag": "yellow",
        "start_time": "00:10"
    }

    alerts = process_alerts(flag_changes)

    assert len(alerts) == 1
    assert alerts[0]["type"] == "incident"
    assert "yellow flag lasted 35s" in alerts[0]["message"]