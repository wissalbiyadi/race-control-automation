# 🏎️ Race Control Automation

[![Streamlit App](https://img.shields.io/badge/🚀%20Live%20App-Streamlit-blue?logo=streamlit&logoColor=white)](https://race-control-automation.streamlit.app)

A real-time dashboard simulating F1 race control using sector flag data. Monitors flag changes and generates automated alerts. Includes fallback to mock data when live API is unreachable or incomplete.

---

## 📺 Live Demo

**🔗 Deployed App:** [Try the Dashboard](https://race-control-automation.streamlit.app/)

---

## 🚀 Features

- Real-time session monitoring from OpenF1 API
- Fallback to mock data when:
  - Live API is down
  - API returns unexpected structure (e.g. missing `sector_flags`)
- Alerts for:
  - Red flags (session suspension)
  - Long yellow flags (auto-logged incidents)
- Developer Debug Panel: inspect raw API response if fallback is triggered
- Automated tests for flag logic and data structure

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit** – Interactive UI
- **Requests** – API integration
- **Pandas** – (reserved for possible future use)
- **BeautifulSoup** – (installed, not yet used)
- **Pytest** – Unit testing

---

## 📂 Project Structure

```
├── data
│   └── mock_live_timing.json         # Fallback race data
├── src
│   ├── alerts.py                     # Alert logic
│   ├── data_feed.py                  # Data loading (mock + live)
│   ├── flag_logic.py                 # Sector flag change detection
│   └── logger.py                     # Optional logging helpers
├── ui
│   └── dashboard.py                  # Streamlit app entry point
├── tests
│   ├── test_alerts.py
│   ├── test_flag_logic.py
│   └── test_data_feed.py            # ✅ Added test for fallback logic
├── requirements.txt
└── README.md
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/wissalbiyadi/race-control-automation
cd race-control-automation
pip install -r requirements.txt
streamlit run ui/dashboard.py
```

---

## 📝 License

MIT

---

## 🙋‍♀️ Author

Made with ❤️ by Wissal Biyadi

Feel free to connect or give feedback!