from ditto import readConfig, getFilename

def getBaseConfig(domain, dns):
    config = """
    # dhcpd.conf

    option domain-name "%s";
    option domain-name-servers %s;
    default-lease-time 3600;
    max-lease-time 7200;
    set vendor-string = option vendor-class-identifier;
    ddns-update-style none;
    authoritative;
    log-facility local7;
    """ % (domain, dns)
    return config

def getTftpConfig(tftpServer, fileName):
    config = """
    next-server %s;
    filename "%s";
    """ % ( tftpServer, fileName)
    return config

def createTableSubnet(name, switch, tftpServer):
    config = """
    subnet %s netmask %s {
      range %s %s;
      option routers %s;
      next-server %s;
      if substring (option vendor-class-identifier, 0, 9) = "docsis1.0" {
          filename "cisco/%s";
      }
    }
    """ % (switch["network"], switch["netmask"], switch["to"], switch["from"], switch["gateway"], tftpServer, name)
    return config


def main():

    fn = getFilename() 
    conf = readConfig(fn)

    output = getBaseConfig(conf["general"]["domain"], conf["general"]["dns-master"])
    output += getTftpConfig(conf["general"]["tftp"], conf["general"]["pxefile"])
    for switch in conf["switch"]:
        output += createTableSubnet(switch, conf["switch"][switch], conf["general"]["tftp"])
    print(output)

main()
