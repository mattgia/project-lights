from scapy.all import sniff

known_devices = set()

def handle_arp_packet(packet):
    src = packet.src
    if src != 'ff:ff:ff:ff:ff:ff':
        known_devices.add(packet.src)

    print(known_devices)

if __name__ == "__main__":
    sniff(filter="arp", prn=handle_arp_packet)