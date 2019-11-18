#!/usr/bin/env

import scapy.all as scapy

def scan(ip):
  arp_request = scapy.ARP(pdst=ip) 
  arp_request.show()
  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  broadcast.show()
  arp_request_broadcast = broadcast/arp_request
  arp_request_broadcast.show()
  answeredlist, unansweredlist = scapy.srp(arp_request_braodcast)
  # to list variables in scapy Ether 
  scapy.ls(Ether)
#list out the answered responses  
  print(answeredlist.summary())
  
scan("192.168.0.0/16")
        
