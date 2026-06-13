# Wi-Fi Deauthentication Attack Detector

A real-time Python tool that monitors 802.11 management frames and detects Wi-Fi deauthentication/disassociation attacks using sliding window threshold analysis.

---

## How Deauth Attacks Work

802.11 management frames (deauth/disassoc) are **unauthenticated by design** in WPA2 and older protocols.
An attacker can spoof any MAC address and flood a network with deauth frames, forcibly disconnecting clients.

**Common use cases by attackers:**
- Force WPA handshake capture (for offline password cracking)
- Evil Twin / Rogue AP setup
- Denial of Service against Wi-Fi clients

> WPA3 fixes this with Protected Management Frames (PMF), but most networks still run WPA2.

---

## Features

- Detects deauth (subtype 12) and disassociation (subtype 10) floods
- Sliding time-window based threshold detection
- Real-time terminal alerts with attacker MAC and frame count
- JSON logging of all detected events
- PCAP replay mode — no hardware needed for testing
- Synthetic attack simulator included

---

## Project Structure
wifi-deauth-detector/
├── detector.py        # Core sniffer + detection engine

├── alerter.py         # Alert formatter and trigger

├── logger.py          # JSON log writer

├── config.py          # Thresholds and interface config

├── simulator.py       # Generates test PCAP with deauth frames

├── requirements.txt

└── deauth_log.json    # Auto-created on first detection

---

## Requirements

- Python 3.8+
- Scapy
- Kali Linux / Ubuntu (for live mode)
- Compatible Wi-Fi adapter with monitor mode support (live mode only)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

### Mode 1 — PCAP Replay (No Hardware Needed)

```bash
# Generate simulated attack traffic
python3 simulator.py

# Run detector against it
python3 detector.py simulated_deauth.pcap
```

### Mode 2 — Live Monitor Mode (Requires Compatible Wi-Fi Adapter)

```bash
# Enable monitor mode
sudo airmon-ng check kill
sudo airmon-ng start wlan0

# Run detector
sudo python3 detector.py
```

---

## Configuration

Edit `config.py` to tune detection sensitivity:

| Parameter    | Default  | Description                            |
|-------------|----------|----------------------------------------|
| THRESHOLD   | 10       | Frames from one MAC to trigger alert   |
| TIME_WINDOW | 5        | Sliding window in seconds              |
| INTERFACE   | wlan0mon | Monitor mode interface                 |
| LOG_FILE    | deauth_log.json | Output log file                 |

---

## Sample Output---

## Requirements

- Python 3.8+
- Scapy
- Kali Linux / Ubuntu (for live mode)
- Compatible Wi-Fi adapter with monitor mode support (live mode only)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Usage

### Mode 1 — PCAP Replay (No Hardware Needed)

```bash
# Generate simulated attack traffic
python3 simulator.py

# Run detector against it
python3 detector.py simulated_deauth.pcap
```

### Mode 2 — Live Monitor Mode (Requires Compatible Wi-Fi Adapter)

```bash
# Enable monitor mode
sudo airmon-ng check kill
sudo airmon-ng start wlan0

# Run detector
sudo python3 detector.py
```

---

## Configuration

Edit `config.py` to tune detection sensitivity:

| Parameter   | Default | Description                             |
|-------------|----------|----------------------------------------|
| THRESHOLD   | 10       | Frames from one MAC to trigger alert   |
| TIME_WINDOW | 5        | Sliding window in seconds              |
| INTERFACE   | wlan0mon | Monitor mode interface                 |
| LOG_FILE    | deauth_log.json | Output log file                 |

---

## Sample Output
[!] ALERT [2026-06-13 04:39:20]

Type   : DEAUTH

Source : aa:bb:cc:dd:ee:ff

Count  : 10 frames in window
---

## Sample Log (deauth_log.json)

```json
[
  {
    "timestamp": "2026-06-13 04:39:20",
    "type": "DEAUTH",
    "src_mac": "aa:bb:cc:dd:ee:ff",
    "count": 10
  }
]
```

---

## Skills Demonstrated

- 802.11 frame structure and management frame parsing
- Raw packet capture and analysis with Scapy
- Sliding window anomaly detection algorithm
- Structured JSON logging
- PCAP generation and replay
- Offensive and defensive security thinking

---

## Legal Disclaimer

This tool is intended **only** for use on networks you own or have explicit written permission to monitor.
Unauthorized network monitoring may violate local laws and regulations.
The author assumes no liability for misuse of this tool.

---

## Author

**Akshara Alagarsamy**
Cyber Security Student @ Sri Krishna College of Technology
[LinkedIn](https://www.linkedin.com/in/akshara-alagarsamy-122861290) • [GitHub](https://github.com/AksharaAlagarsamy)
