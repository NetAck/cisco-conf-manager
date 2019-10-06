import argparse
import ipaddress



class Static_ipv4_range:
    def __init__(self, interface_range, ip, mask = "0",  shutdown = False):
        self.interface_range = interface_range
        self.ip_address = ipaddress.ip_address(ip)
        if mask == 0:
            a = ipaddress.ip_network(ip).with_netmask.split('/')
            mask = a[1]
        self.mask = mask
        self.shutdown = check_shutdown(shutdown)

def check_shutdown(shutdown):
    if (shutdown == 1):
        return "no "
    return ""

def generate_command(self):
    s = f"""\

interface range {self.interface_range}
ip address {self.ip_address} {self.mask}
{self.shutdown}shutdown
exit\

    """
    return s

def append_to_file(self, filename = "interface-range-config.txt"):
    file = open(filename, "a")
    success = file.write(generate_command(self))
    file.close
    return success

        

def main():
    parser = argparse.ArgumentParser()
    parser.usage = 'Usage: python3 router.py ' + '-i <interface range> -n <network ip> -m <mask> -s <shutdown status> -f <file to output>'
    required = parser.add_argument_group('required arguments')
    required.add_argument('-i', '--interface', action='store', type=str, help='specify the default router', required=True)
    required.add_argument('-n', '--netIp', action='store', type=str, help='specify network ip', required=True)
    required.add_argument('-m', '--mask', action='store', type=str, help='network mask', required=True)
    required.add_argument('-s', '--shutdown', type=bool, action='store_true', help='specify if the interface is shutted down or not', required=False)
    required.add_argument('-f', '--file', type=str, action='store', help='specify the file to generate/append', required=True)
    args = parser.parse_args()

    if args.netIp is None \
            or args.interface is None:
        print(parser.usage)
        exit(0)

    # Create Static IPv4 Interface Object
    static_ipv4_range = Static_ipv4_range(args.interface, args.netIp, args.mask, args.shutdown)
    if (append_to_file(static_ipv4_range, args.file)):
        print("Configuration Generated and Stored/Appended with sucess")
    else:
        print("Error while generating/appending the file. Invalid parameters")

if __name__ == '__main__':
    main()
