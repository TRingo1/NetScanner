#!/usr/bin/env

import scapy.all as scapy

def scan(ip):
  arp_request = scapy.ARP(pdst=ip) 
  #arp_request.show()
  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  #broadcast.show()
  arp_request_broadcast = broadcast/arp_request
  #arp_request_broadcast.show()
  answeredlist = scapy.srp(arp_request_braodcast, timeout=1, verbose=False)[0]
  # to list variables in scapy Ether 
  scapy.ls(Ether)
#list out the answered responses  
#  print(answeredlist.summary())
print("IP\t\t\tMAC Address\n_______________________________________________")
# list all elements
for element in answered_list:
  print(element[1].psrc + "\t\t" +element[1].hwsrc)

scan("192.168.0.0/16")
        
