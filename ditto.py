import json
import argparse

def readConfig(jsonFile):
    f = open(jsonFile, 'r').read()
    return json.loads(f)

def getFilename():
    parser = argparse.ArgumentParser(description='Create DHCP config from JSON')
    parser.add_argument('--file', '-f', dest='filename', required=True,
                    help='JSON file with LAN config')
    args = parser.parse_args()
    return args.filename

def getSubnetAddress(maskBits):
    bits = []
    string = ""
    c = 0
    while c < 32:
        if c < maskBits:
            string += "1"
        else:
            string += "0"
        if len(string) == 8:
            bits.append(string)
            string = ""
        c += 1
    bits = list(map(lambda x: str(int(x,2)), bits))
    return ".".join(bits)
