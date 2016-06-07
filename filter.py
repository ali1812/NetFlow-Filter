#!/usr/bin/env python
# Copyright (c) 2016 Ali Al-Habsi

from scapy.all import *

#read packets from the pcap file
packets = rdpcap('slowdownload.pcap')

#parse packets into flows
flows = packets.sessions()

# this function extract flows with 60 or more packets.
def return_first_packet():
    pckts = []
    for keys, values in flows.items():
        if (len(values) >=60):
            print keys
            print len(values)
        #Append first packet to packetlist pckts
            pckts +=[values[0]]
            
    wrpcap("test.pcap",pckts)

            
return_first_packet()
