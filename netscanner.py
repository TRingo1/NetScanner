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

clients_list = []
for element in answered_list:
  client_dict = {"ip" : element[1].psrc, "mac": element[1].hwsrc}
  client_list.append(client_dict)
return (client_list)

def print_results(results_list)
    print("IP\t\t\tMAC Address\n_______________________________________________")
    for client in results_list:
      print(client["ip"] + "\t\t" + client["mac"])
  
scan_result = scan("192.168.0.0/16")
print_result(scan_result)        
