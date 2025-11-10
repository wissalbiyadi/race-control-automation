def detect_flag_changes(prev_frame, current_frame):
    """
    Compares two frames and returns a list of flag state changes.
    Each change is a dictionary with sector, from_flag, to_flag.
    """
    changes = []
    prev_flags = prev_frame["sector_flags"] if prev_frame else {}

    for sector, current_flag in current_frame["sector_flags"].items():
        prev_flag = prev_flags.get(sector, None)

        if prev_flag and prev_flag != current_flag:
            changes.append({
                "sector": sector,
                "from": prev_flag,
                "to": current_flag,
                "time": current_frame["time"]
            })

    return changes