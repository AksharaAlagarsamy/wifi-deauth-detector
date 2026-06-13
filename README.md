# Wi-Fi Deauth Attack Detector

A Python tool that monitors 802.11 management frames and detects
Wi-Fi deauthentication/disassociation attacks in real time.

## How Deauth Attacks Work

802.11 management frames (like deauth/disassoc) are **unauthenticated
by design** in WPA2 and older. An attacker can spoof any MAC address
and flood a network with deauth frames, forcibly disconnecting clients.
This is commonly used in:
- Evil Twin / rogue AP attacks
- WPA handshake capture (forces reauthentication)
- Denial of Service against Wi-Fi clients

WPA3 fixes this with Protected Management Frames (PMF), but most
networks still run WPA2.

## Features

- Detects deauth (subtype 12) and disassociation (subtype 10) floods
- Sliding time-window based threshold detection
- Real-time terminal alerts with attacker MAC and frame count
- JSON logging of all detected events
- PCAP replay mode for testing without hardware
- Synthetic attack simulator included

## Project Structure
wifi-deauth-detector/

├── detector.py      # Core sniffer + detection engine

├── alerter.py       # Alert formatter + trigger

├── logger.py        # JSON log writer

├── config.py        # Thresholds and interface config

├── simulator.py     # Generates test PCAP with deauth frames

└── deauth_log.json  # Auto-created on first detection## Requirements

- Python 3.8+
- scapy

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Mode 1 — PCAP Replay (no hardware needed)
```bash
# Generate simulated attack traffic
python3 simulator.py

# Run detector against it
python3 detector.py simulated_deauth.pcap
```

### Mode 2 — Live Monitor Mode (requires compatible Wi-Fi adapter)
```bash
sudo airmon-ng check kill
sudo airmon-ng start wlan0
sudo python3 detector.py
```

## Configuration

Edit `config.py` to tune detection sensitivity:

| Parameter    | Default | Description                          |
|-------------|---------|--------------------------------------|
| THRESHOLD   | 10      | Frames from one MAC to trigger alert |
| TIME_WINDOW | 5       | Sliding window in seconds            |
| INTERFACE   | wlan0mon| Monitor mode interface               |

## Sample Output[!] ALERT [2026-06-13 04:39:20]

Type   : DEAUTH

Source : aa:bb:cc:dd:ee:ff

Count  : 10 frames in window## Legal Disclaimer

This tool is intended for use on networks you own or have explicit
written permission to monitor. Unauthorized network monitoring may
violate local laws. The author assumes no liability for misuse.

## Skills Demonstrated

- 802.11 frame structure and management frame parsing
- Raw socket programming with Scapy
- Sliding window anomaly detection
- Structured JSON logging
- Offensive/defensive security thinking
