from scapy.all import ARP, Ether, sniff
import time

def handle_arp_packet(packet):
    is_arp = packet
    print(is_arp)
    print(dir(is_arp))
    op = is_arp.op if is_arp else None
    if op == ARP.who_has:
        print('New ARP Request')
        print(packet.summary())
        print(packet[Ether].src, "has IP", packet[ARP].psrc)
    elif op == ARP.is_at:
        print('New ARP Reply')
        print(packet.summary())
    else:
        print('No op found')

    return

if __name__ == "__main__":
    sniff(filter="arp", prn=handle_arp_packet)