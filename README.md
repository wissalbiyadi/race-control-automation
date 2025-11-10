# 🏁 Race Control Automation

A Python-based simulation of an FIA-style Race Control system for motorsport operations.

## 💡 What It Does
- Reads simulated live sector flag data
- Detects flag changes (green → yellow, yellow → red)
- Logs all flag events and alerts
- Triggers race control alerts (e.g. yellow > 30s = incident log, red = suspend session)
- Displays real-time GUI using Streamlit

## 🧠 Technologies Used
- Python
- Streamlit (GUI)
- Pytest (Testing)
- JSON (Mock live timing data)

## 📂 Project Structure

```
race-control-automation/
├── src/                  # Core backend logic (flags, alerts, data)
├── ui/                   # Streamlit dashboard
├── data/                 # Mock live timing feed
├── tests/                # Pytest test suite
├── venv/                 # Virtual environment (ignored by .gitignore)
├── requirements.txt      # Dependencies
└── README.md             # Project overview
```

## ▶️ How to Run

```bash
# 1. Clone the repo

# 2. Create and activate a virtual environment

# 3. Install dependencies:
pip install -r requirements.txt

# 4. Run the dashboard:
streamlit run ui/dashboard.py
```

## 🧪 Run Tests

```bash
pytest tests/
```

---

✅ Built for aspiring motorsport engineers, operations analysts, and automation developers looking to showcase rule-based systems for Race Control or stewarding simulation.
