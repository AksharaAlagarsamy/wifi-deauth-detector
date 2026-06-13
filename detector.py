from scapy.all import sniff, Dot11, Dot11Deauth, Dot11Disas
from collections import defaultdict
import time
from config import THRESHOLD, TIME_WINDOW
from alerter import trigger_alert

frame_counts = defaultdict(list)

def process_frame(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype in (10, 12):
            src = pkt.addr2
            now = time.time()
            frame_counts[src] = [
                t for t in frame_counts[src]
                if now - t < TIME_WINDOW
            ]
            frame_counts[src].append(now)
            count = len(frame_counts[src])
            if count >= THRESHOLD:
                trigger_alert(src, pkt.subtype, count)

def start_sniffing(pcap_file=None):
    if pcap_file:
        print(f"[*] Reading from {pcap_file}...")
        sniff(offline=pcap_file, prn=process_frame, store=False)
    else:
        from config import INTERFACE
        print(f"[*] Listening on {INTERFACE}...")
        sniff(iface=INTERFACE, prn=process_frame, store=False)

if __name__ == "__main__":
    import sys
    pcap = sys.argv[1] if len(sys.argv) > 1 else None
    start_sniffing(pcap)
