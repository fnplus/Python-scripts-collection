"""
This script retrieves information about IP addresses an generates a CSV file out of it
 
Put a list of IPs in ip_list.txt in current directory (plain IPs, one per line)
CSV output is written to out_file.csv in current directory

Lookups are retrieved from extreme-ip-lookup.com website
"""
import csv
import getpass
import socket

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

session = requests.session()
session.verify = False

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

with open("out_file.csv", mode="w", newline='') as out_file, open('ip_list.txt') as ip_list:
    out_file.write("SEP=,\n")

    csvwriter = csv.writer(out_file)
    csvwriter.writerow([
        "IP",
        "Name",
        "Location",
        "LookupName",
        "ISP",
        "Organization",
    ])

    for ip in ip_list.readlines():
        ip = ip.strip()
        try:
            hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
        except:
            hostname = ''

        try:
            response = session.get("https://extreme-ip-lookup.com/json/%s" % ip)
            response.raise_for_status()
            ip_data = response.json()

            location = ip_data['country'] + ' ' + ip_data['continent']
            ipName = ip_data['ipName']
            isp = ip_data['isp']
            org = ip_data['org']
        except:
            location = ''
            ipName = ''
            isp = ''
            org = ''

        print('%-20s%s' % (ip, hostname))
        csvwriter.writerow([
            ip,
            hostname,
            location,
            ipName,
            isp,
            org,
        ])
