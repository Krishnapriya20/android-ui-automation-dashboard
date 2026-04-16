# Android UI Automation Dashboard

##  Project Overview

This project automates Android app form filling using ADB (Android Debug Bridge) and visualizes the results through an interactive dashboard.

It simulates real user actions like tapping, scrolling, and typing, and logs each operation as Success or Fail.

---

##  Features

* Automated mobile UI interaction using ADB
* CSV-based bulk data entry (multiple users)
* Interactive dashboard with charts & metrics
* Search and filter functionality
* Downloadable report
* Success/Failure tracking

---

## Tech Stack

* Python
* ADB (Android Debug Bridge)
* Streamlit
* Pandas
* Matplotlib

---

## How It Works

1. Data is read from a CSV file
2. ADB performs UI actions on the Android device
3. Each entry is logged in a report
4. Dashboard displays the results visually

---

## How to Run

### Step 1: Run Automation

```
python main.py
```

### Step 2: Run Dashboard

```
streamlit run dashboard.py
```

---

## Dashboard Preview

(Add your screenshot here)

![Dashboard Screenshot](screenshot.png)

---

## Project Structure

```
main.py
actions.py
adb_controller.py
config.yaml
dashboard.py
test_data.csv
report.csv
requirements.txt
```

---

## 👩‍💻 Author

Krishnapriya B

---

## Highlights

* End-to-end automation system
* Real-time dashboard visualization
* Practical use of ADB for UI automation
