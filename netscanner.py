#!/usr/bin/env

import scapyall as scapy

def scan(ip):
  arp_request = scapy.ARP()  
  print(arp_requst.summary())   
         
scan("192.168.0.0/16")
        
