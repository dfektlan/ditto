from ditto import readConfig, getFilename, getSubnetAddress
import ipaddress

def getRouter(servers):
    for server in servers:
        if servers[server]['role'] == 'router':
            return servers[server]
    return None

def generateInterfaceAddresses(router, pubnet):
    ipnet = ipaddress.ip_network(pubnet)
    subnetmask = getSubnetAddress(int(pubnet[-2:]))
    output = ""
    for ip in ipnet.hosts():
        output += ("ip addr add %s/%s broadcast %s dev %s\n" % (str(ip), pubnet[-2:], subnetmask, router["pub_int"]))
    return output

def main():
    fn = getFilename()
    conf = readConfig(fn)

    router = getRouter(conf["server"])
    pubnet = conf['general']['pubnet']

    print(generateInterfaceAddresses(router, pubnet))

main()
