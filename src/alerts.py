import datetime

# Keep track of when sectors go yellow or red
active_flags = {}

def process_alerts(flag_changes):
    alerts = []
    current_time = None

    for change in flag_changes:
        sector = change["sector"]
        from_flag = change["from"]
        to_flag = change["to"]
        current_time = change["time"]

        # Start timer if yellow or red is activated
        if to_flag in ["yellow", "red"]:
            active_flags[sector] = {
                "flag": to_flag,
                "start_time": current_time
            }

        # If going back to green, check how long it was yellow/red
        elif to_flag == "green" and sector in active_flags:
            entry = active_flags.pop(sector)
            duration = calculate_duration(entry["start_time"], current_time)

            if entry["flag"] == "yellow" and duration > 30:
                alerts.append({
                    "type": "incident",
                    "message": f"{sector} yellow flag lasted {duration}s — auto-log incident",
                    "time": current_time
                })
            elif entry["flag"] == "red":
                alerts.append({
                    "type": "race_control",
                    "message": f"{sector} red flag cleared at {current_time}",
                    "time": current_time
                })

        # If red flag just deployed
        if to_flag == "red":
            alerts.append({
                "type": "race_control",
                "message": f"RED FLAG in {sector} at {current_time} — suspend session",
                "time": current_time
            })

    return alerts

def calculate_duration(start, end):
    """Takes start and end times like '00:25', returns duration in seconds"""
    t1 = datetime.datetime.strptime(start, "%M:%S")
    t2 = datetime.datetime.strptime(end, "%M:%S")
    delta = t2 - t1
    return int(delta.total_seconds())