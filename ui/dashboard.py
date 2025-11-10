import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.data_feed import load_mock_data
from src.flag_logic import detect_flag_changes
from src.alerts import process_alerts

# Initialise state
if "frame_index" not in st.session_state:
    st.session_state.frame_index = 0
    st.session_state.previous_frame = None
    st.session_state.alerts = []
    st.session_state.log = []

# Load mock data
data = load_mock_data()

# Title
st.title("🏁 Race Control Dashboard")
st.caption("Live flag monitoring and alert simulation")

# Get current frame
if st.session_state.frame_index < len(data):
    frame = data[st.session_state.frame_index]
    changes = detect_flag_changes(st.session_state.previous_frame, frame)

    # Display sector status
    st.subheader(f"⏱️ Time: {frame['time']}")
    for sector, flag in frame["sector_flags"].items():
        st.markdown(f"- **{sector.capitalize()}**: `{flag.upper()}`")

    # Handle changes
    for change in changes:
        msg = f"[{change['time']}] {change['sector']} {change['from']} → {change['to']}"
        st.session_state.log.append(msg)

    # Process alerts
    alerts = process_alerts(changes)
    for alert in alerts:
        alert_msg = f"[{alert['time']}] 🚨 {alert['message']}"
        st.session_state.alerts.append(alert_msg)

    st.session_state.previous_frame = frame
    st.session_state.frame_index += 1
else:
    st.warning("🚧 End of mock race data.")

# Log history
with st.expander("📝 Event Log"):
    for entry in st.session_state.log:
        st.write(entry)

# Alert history
st.subheader("⚠️ Alerts")
for alert in reversed(st.session_state.alerts[-5:]):  # last 5
    st.error(alert)

# Auto-refresh every 2 seconds
st.rerun()