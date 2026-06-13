from scapy.all import RadioTap, Dot11, Dot11Deauth, wrpcap

frames = []
for i in range(30):
    pkt = (
        RadioTap() /
        Dot11(
            type=0, subtype=12,
            addr1="ff:ff:ff:ff:ff:ff",
            addr2="aa:bb:cc:dd:ee:ff",
            addr3="00:11:22:33:44:55"
        ) /
        Dot11Deauth(reason=7)
    )
    frames.append(pkt)

wrpcap("simulated_deauth.pcap", frames)
print("[+] simulated_deauth.pcap created with 30 deauth frames.")
