from data_feed import load_mock_data, load_live_data, simulate_live_feed

USE_LIVE_DATA = False  # ← You can change this later

if USE_LIVE_DATA:
    data = load_live_data()
else:
    data = load_mock_data()

from flag_logic import detect_flag_changes
from alerts import process_alerts
from logger import init_log, log_flag_change, log_alert

def main():
    print("🚦 Race Control System Starting...\n")
    init_log()

    data = load_mock_data()
    previous_frame = None

    for frame in simulate_live_feed(data, delay=2):  # Simulate real-time every 2s
        flag_changes = detect_flag_changes(previous_frame, frame)

        for change in flag_changes:
            log_flag_change(change)

        alerts = process_alerts(flag_changes)

        for alert in alerts:
            log_alert(alert)

        previous_frame = frame

if __name__ == "__main__":
    main()