from scapy.all import IP, ICMP, sr1

packet = IP(dst="127.0.0.1") / ICMP()

reply = sr1(packet, timeout=2, verbose=False)

if reply:
    print("ICMP Reply Received")
    print("-------------------")
    print("Source IP      :", reply[IP].src)
    print("Destination IP :", reply[IP].dst)
    print("ICMP Type      :", reply[ICMP].type)
    print("ICMP Code      :", reply[ICMP].code)
    print("TTL            :", reply[IP].ttl)
else:
    print("No reply received")
