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

