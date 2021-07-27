#! /usr/bin/env python3

import sys
import re
import nmap
import nmapthon as scan


scanner = scan.NmapScanner('10.0.0.0/24', ports=22)

try:
    scanner.run()
except scan.NmapScanError as error:
   print('Error!')

for host in scanner.scanned_hosts():
   print("Hostname: {}".format(','.join(scan.hostnames(host))))

#print("Start Timestamp: {} ".format(scanner.start_timestamp))
print("Start Time: {} ".format(scanner.start_time))
print("Exit Status: {} ".format(scanner.exit_status))
print("Arguments: {} ".format(scanner.args))
print("Summary: {} ".format(scanner.summary))
#print("Version: {} ".format(scanner.version))
#print("End Timestamp: {} ".format(scanner.end_timestamp))
print("End Time: {} ".format(scanner.end_time))
print("Finished? {} ".format(scanner.finished))
print("Tolerant Errors: {} ".format(scanner.tolerant_errors))

