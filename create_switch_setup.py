import ipaddress
import json
from pprint import pprint
from math import log, ceil
from ditto import getSubnetAddress



rows = int(input("Number of rows: "))
per = int(input("Switches per tables: "))
switchMaskBit = int(input("Mask bit for each switch: ")) 
switchNetworkStart = input("Start address for the participant network: ")
totalNetworkSize = 32-(ceil(log(per*rows*(2**(32-switchMaskBit)),2)))
vendorIdentifier = "docsis1.0"
networks = list(ipaddress.ip_network("%s/%d" % (switchNetworkStart, totalNetworkSize)).subnets(new_prefix=switchMaskBit))


s = {}
s["switch"] = {}
c = 0
for row in range(1, rows+1):
    for p in range(1, per+1):
        c += 1
        name = "row-%d-%d" % (row, p)
        ipnet = networks.pop(0)
        s["switch"][name] = {
            "port": c,
            "ip": str(ipnet[2]),
            "netmask": getSubnetAddress(switchMaskBit),
            "gateway": str(ipnet[1]),
            "bit": switchMaskBit,
            "from": str(ipnet[3]),
            "to": str(ipnet[-2]),
            "vendor-identifier": vendorIdentifier,
            "network": str(ipnet[0])
        }

print(json.dumps(s, indent=4, separators=(',', ': ')))

