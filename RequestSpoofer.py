from scapy.all import *
print("UDP Req Spoofer - [IlkaySolotov]")
srca = input("Enter source ip: ")
dsta = input("Enter target ip: ")
scrp = 9090
dstp = 9090
addy=IP(src=srca, dst=dsta)
prot=UDP(sport=scrp,dport=dstp)
buf="Spoofed Req By github.com/IlkaySolotov"
pkt=addy/prot/buf
pkt.show()
send(pkt,verbose=0)
