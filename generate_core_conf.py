from ditto import readConfig, getFilename
from jinja2 import Template


def generateCoreConfig(ports, hostname, ip, subnet, gateway, template):
    temp = Template(open(template, 'r').read())
    print(temp.render(
        tableports = ports,
        hostname = hostname,
        ip = ip,
        subnet = subnet,
        gateway = gateway
    ))

def generatePort(name, switch, dhcpserver):
    port = """
    interface GigabitEthernet0/%s
     description %s
     no switchport
     ip address %s %s
     ip helper-address %s
    !
    """ % (switch['port'], name, switch['gateway'], switch['netmask'], dhcpserver)
    return port




def main():

    fn = getFilename() 
    conf = readConfig(fn)

    ports = ""
    for switch in conf["switch"]:
        ports += generatePort(switch, conf["switch"][switch], conf['general']['dhcp'])
    generateCoreConfig(ports, 'core', conf['general']['core'], '255.255.255.128', conf['general']['gateway'], 'template/c3560g.txt')

main()
