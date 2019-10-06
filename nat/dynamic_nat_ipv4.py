import argparse
import ipaddress



class Dynamic_nat_ipv4:
    def __init__(self, inside_interface, outside_interface, pool_name, start_ip, end_ip, acl_number, source_ip, source_wildcard = "", mask = ""):
        self.pool_name = pool_name
        self.start_ip = ipaddress.IPv4Address(start_ip)
        self.end_ip = ipaddress.IPv4Address(end_ip)
        if(mask != ""):
            self.mask = "prefix-length " + ipaddress.IPv4Network.prefixlen(start_ip + "/" + mask)
        else:
            self.mask = mask
        self.acl_number = acl_number
        self.source_ip = ipaddress.IPv4Address(source_ip)
        if (source_wildcard != ""):  
            self.source_wildcard = ipaddress.IPv4Network.hostmask(source_wildcard)
        else:
            self.source_wildcard = source_wildcard
        self.inside_interface = inside_interface
        self.outside_interface = outside_interface


def generate_command(self):
    s = f"""\

ip nat pool {self.pool_name} {self.start_ip} {self.end_ip} {self.mask}        
access-list {self.acl_number} permit {self.source_ip} {self.source_wildcard}
ip nat inside source list {self.acl_number} pool {self.pool_name}
interface {self.inside_interface}
ip nat inside
exit
interface {self.outside_interface}
ip nat outside
exit\

    """
    return s

def append_to_file(self, filename = "dynamic-nat-config.txt"):
    file = open(filename, "a")
    success = file.write(generate_command(self))
    file.close
    return success

        

def main():
    parser = argparse.ArgumentParser()
    parser.usage = 'Usage: python3 router.py ' + '-p <pool name> -s <start ip address> -e <end ip address> [-m <network mask>] -a <acl number> -S <acl source ip address> [-w <source wildcard>] -i <inside interface> -o <outside interface> -f <file to output>'
    required = parser.add_argument_group('required arguments')
    required.add_argument('-p', '--pool', action='store', type=str, help='specify the pool name', required=True)
    required.add_argument('-s', '--start_ip', action='store', type=str, help='specify the first ip address of the pool', required=True)
    required.add_argument('-e', '--end_ip', action='store', type=str, help='specify the last ip address of the pool', required=True)
    required.add_argument('-e', '--mask', action='store', type=str, help='specify the network mask of the pool', required=False)
    required.add_argument('-a', '--acl', action='store', type=str, help='specify the acl number', required=True)
    required.add_argument('-S', '--acl_source', action='store', type=str, help='specify the acl source ip', required=True)
    required.add_argument('-w', '--source_wildcard', action='store', type=str, help='specify the acl source wildcard', required=False)
    required.add_argument('-i', '--inside', action='store', type=str, help='specify the inside interface', required=True)
    required.add_argument('-o', '--outside', action='store', type=str, help='specify the outside interface', required=True)
    required.add_argument('-f', '--file', type=str, action='store', help='specify the file to generate/append', required=True)
    args = parser.parse_args()

    if args.inside is None \
            or args.pool is None \
            or args.start_ip is None \
            or args.end_ip is None \
            or args.acl is None \
            or args.acl_source is None \
            or args.file is None \
            or args.outside is None:
        print(parser.usage)
        exit(0)

    # Create Static IPv4 Interface Object
    dynamic_nat_ipv4 = Dynamic_nat_ipv4(args.inside, args.outside, args.pool_name, args.start_ip, args.end_ip, args.mask, args.acl, args.source_ip, args.source_wildcard)
    if (append_to_file(dynamic_nat_ipv4, args.file)):
        print("Configuration Generated and Stored with sucess")
    else:
        print("Error while generating/appending the file. Invalid parameters")

if __name__ == '__main__':
    main()