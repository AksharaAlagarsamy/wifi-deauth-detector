from datetime import datetime
from logger import write_log

def trigger_alert(src_mac, subtype, count):
    frame_type = "DEAUTH" if subtype == 12 else "DISASSOC"
    timestamp  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    msg = (
        f"\n[!] ALERT [{timestamp}]\n"
        f"    Type   : {frame_type}\n"
        f"    Source : {src_mac}\n"
        f"    Count  : {count} frames in window\n"
    )
    print(msg)
    write_log({"timestamp": timestamp, "type": frame_type,
               "src_mac": src_mac, "count": count})
