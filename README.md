# pyarpspoof

Pyarpspoof is a simple arp spoofer written in python(works with python3) for linux machines which takes a target ip and gateway ip as an input.


What Is ARP Spoofing?

ARP spoofing is a type of attack in which a malicious actor sends falsified ARP (Address Resolution Protocol) messages over a local area network. This results in the linking of an attacker’s MAC address with the IP address of a legitimate computer or server on the network. Once the attacker’s MAC address is connected to an authentic IP address, the attacker will begin receiving any data that is intended for that IP address. ARP spoofing can enable malicious parties to intercept, modify or even stop data in-transit. ARP spoofing attacks can only occur on local area networks that utilize the Address Resolution Protocol.



To allow traffic to pass through your linux machine you need to use the command



echo 1 > /proc/sys/net/ipv4/ip_forward

Usage:
Run the python script and it asks for a target ip and gateway ip
incase if you dont know gatewayip use route -n to find out
EXAMPLE:

python3 pyarpspoof.py
