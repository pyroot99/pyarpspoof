# pyarpspoof

Pyarpspoof is a simple arp spoofer written in python(works with python3) for linux machines which takes a target ip and gateway ip as an input and tells the gateway that the target ip is your machines ip and tells the target that the gateway ip is your machines ip which makes you the man in the middle.



To allow traffic to pass through your linux machine you need to use the command



echo 1 > /proc/sys/net/ipv4/ip_forward

