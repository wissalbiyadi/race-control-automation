import os

LOG_FILE = "race_control_log.txt"

def init_log():
    """Creates or clears the log file at the start of the session."""
    with open(LOG_FILE, 'w', encoding='utf-8') as file:
        file.write("=== RACE CONTROL LOG START ===\n")

def log_flag_change(change):
    log_entry = f"[{change['time']}] FLAG CHANGE: {change['sector']} {change['from']} → {change['to']}"
    print(log_entry)
    write_to_file(log_entry)

def log_alert(alert):
    log_entry = f"[{alert['time']}] ALERT: {alert['message']}"
    print(f"\033[93m{log_entry}\033[0m")  # Yellow colour in terminal
    write_to_file(log_entry)

def write_to_file(text):
    with open(LOG_FILE, 'a', encoding='utf-8') as file:
        file.write(text + "\n")