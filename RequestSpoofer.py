from scapy.all import *
print("UDP Req Spoofer - [IlkaySolotov]")
srca = input("Enter source ip: ")
dsta = input("Enter target ip: ")
scrp = input("Enter source port: ")
dstp = input("Enter target port: ")
addy=IP(src=srca, dst=dsta)
prot=UDP(sport=scrp,dport=dstp)
buf="Spoofed Req By github.com/IlkaySolotov"
pkt=addy/prot/buf
pkt.show()
send(pkt,verbose=0)
