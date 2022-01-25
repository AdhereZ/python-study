import time 
import psutil 

def main():
  traffic_io=psutil.net_io_counters()[:2]
  while True:
    time.sleep(0.5)
    traffic_ioNew