# Amazfit Health Monitor

A real-time wearable health monitoring system that collects health data from an Amazfit smartwatch using Bluetooth Low Energy (BLE), stores the data locally, and displays it through a live dashboard.

This project is designed as a wearable data bridge that can later be integrated into larger healthcare monitoring systems.

---

## Project Objective

The goal of this project is to create a system that can:

- Connect with an Amazfit Bip U Pro smartwatch
- Collect live health-related data
- Store sensor data for later analysis
- Display health parameters through a dashboard
- Provide reusable data for future healthcare projects

---

## Target Device

Current development device:

- Amazfit Bip U Pro
- Bluetooth Low Energy (BLE)

---

## Planned Health Parameters

| Parameter | Status |
|---------|--------|
| Battery Level | Planned |
| Heart Rate | Planned |
| Steps | Planned |
| SpO2 | Planned |
| Stress | Research Phase |

---

## System Architecture

```
Amazfit Smartwatch
        |
        |
 Bluetooth Low Energy
        |
        ↓
 Python BLE Service
        |
        |
        +----------------+
        |                |
        ↓                ↓
 Local Storage      Dashboard
    (CSV)           (Streamlit)

        |
        ↓

 Future Healthcare Systems
```

---

## Tech Stack

### Programming Language
- Python

### Bluetooth Communication
- Bleak (Bluetooth Low Energy)

### Dashboard
- Streamlit

### Data Processing
- Pandas

### Storage
Current:

- CSV

Future:

- Database integration

---

## Project Structure

```
amazfit-health-monitor

│
├── src
│
│   ├── ble
│   │   ├── scanner.py
│   │   ├── connection.py
│   │   ├── collector.py
│   │   └── battery.py
│
│   ├── storage
│   │   └── csv_storage.py
│
│   ├── config.py
│   └── main.py
│

├── dashboard
│   └── app.py
│

├── data

├── docs

├── requirements.txt
├── README.md
└── .gitignore
```

---

## Development Roadmap

### Phase 1 — Project Setup

- [x] Create repository
- [x] Setup virtual environment
- [x] Setup project structure
- [x] Configure Git workflow


---

### Phase 2 — BLE Communication

- [ ] Scan nearby BLE devices
- [ ] Detect Amazfit smartwatch
- [ ] Establish BLE connection
- [ ] Read available services


---

### Phase 3 — Data Collection

- [ ] Battery monitoring
- [ ] Heart rate collection
- [ ] Step data collection
- [ ] SpO2 data collection


---

### Phase 4 — Storage

- [ ] Create storage module
- [ ] Save live sensor data
- [ ] Generate health data logs


---

### Phase 5 — Dashboard

- [ ] Build Streamlit dashboard
- [ ] Show live connection status
- [ ] Display health metrics
- [ ] Visualize historical data


---

## Git Workflow

Development follows feature-based workflow:

```
main
 |
 |
feature/*
 |
 |
Pull Request
 |
 |
main
```

Example:

```
feature/ble-scanner
feature/dashboard
feature/storage
```

---

## Current Status

Project initialization completed.

Currently working on:

```
Feature:
BLE Device Scanner
```

---

## Future Improvements

- Database support
- Edge device integration
- Healthcare monitoring pipeline integration
- Advanced analytics modules

---

## Developer

Maintained by:

**Mayank Balpande**
