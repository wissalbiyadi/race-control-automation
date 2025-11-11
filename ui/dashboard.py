import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.data_feed import load_mock_data, load_live_data
from src.flag_logic import detect_flag_changes
from src.alerts import process_alerts

# Initialise state
if "frame_index" not in st.session_state:
    st.session_state.frame_index = 0
    st.session_state.previous_frame = None
    st.session_state.alerts = []
    st.session_state.log = []

# Load data: Try live data, fallback to mock
USE_LIVE_DATA = True  # Toggle this on/off

data = None

# Load data: Try live API first, fall back if invalid or missing required fields
# Attempt to fetch live data from the OpenF1 API
if USE_LIVE_DATA:
    live_data = load_live_data()

    # Check if the response is a non-empty list and contains dictionary elements
    if isinstance(live_data, list) and len(live_data) > 0 and isinstance(live_data[0], dict):

        # Confirm that the expected structure is present
        if "sector_flags" in live_data[0]:
            # Data format is valid — proceed with live data
            data = live_data
            st.success("✅ Live race data loaded successfully.")
            st.caption("✅ Using real-time data from OpenF1 API.")

        else:
            # API responded, but data structure is not compatible with our app
            st.warning("⚠️ Live API responded, but required structure (e.g. 'sector_flags') is missing.")
            st.info("ℹ️ Reverting to mock data for simulation.")

            # Optional: show raw API response for debugging
            with st.expander("📡 Raw API Response (Developer Debug View)"):
                st.json(live_data)

            data = load_mock_data()
    else:
        # API failed or returned unexpected type — fallback to mock
        st.error("❌ Failed to fetch valid data from the live API.")
        st.info("ℹ️ Reverting to mock data for simulation.")
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