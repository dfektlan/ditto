from ditto import readConfig, getFilename
from jinja2 import Template


def generateTableConfig(name, switch, ports, template):
    temp = Template(open(template, 'r').read())
    f = open('output/tftp/cisco/%s' % name, 'w')
    f.write(temp.render(
        hostname = name,
        ip = switch['ip'],
        subnet = switch['netmask'],
        ports = ports
    ))
    f.close()

def generatePort(number):
    port = """
    interface FastEthernet0/%s
     description %s
     spanning-tree portfast
    !
    """ % (number, number)
    return port

    



def main():

    fn = getFilename() 
    conf = readConfig(fn)

    ports = ""
    for port in range(1,25):
        ports += generatePort(port)
    for switch in conf["switch"]:
        generateTableConfig(switch, conf["switch"][switch], ports, 'template/c2950t.txt')

main()
