import argparse


class Dhcp:
    def __init__(self, net_ip, mask, def_router, dns, domain, lease):
        self.net_ip = net_ip
        self.mask = mask
        self.def_router = def_router
        self.dns = dns
        self.domain = domain
        self.lease = lease

    def generate_dhcp_file(self):
        string_dhcp = f'! Note that you have to be in Configure Terminal Mode\n' \
                      'service dhcp\n' \
                      'ip dhcp pool DHCP-POOL\n' \
                      f'network {self.net_ip} {self.mask}\n' \
                      f'default-router {self.def_router}\n' \
                      f'dns-server {self.dns}\n' \
                      f'domain-name {self.domain}\n' \
                      f'lease {self.lease}\n' \
                      'exit'

        file = open("dhcp-config.txt", "w")
        success = file.write(string_dhcp)
        file.close()
        return success


def main():
    parser = argparse.ArgumentParser()
    parser.usage = 'Usage: python3 dhcp.py ' + '-n <network ip> -m <mask> -r <default router> -d <dns ip> -D <domain name> -l <lease time>'
    required = parser.add_argument_group('required arguments')
    required.add_argument('-n', '--netIp', action='store', type=str, help='specify network ip', required=True)
    required.add_argument('-m', '--mask', action='store', type=str, help='network mask', required=True)
    required.add_argument('-r', '--defRouter', action='store', type=str, help='specify the default router', required=True)
    required.add_argument('-d', '--dns', type=str, action='store', help='specify default dns ip', required=True)
    required.add_argument('-D', '--domain', type=str, action='store', help='specify the domain name', required=True)
    required.add_argument('-l', '--lease', type=str, action='store', help='sepecify lease time', required=False)
    args = parser.parse_args()

    if args.netIp is None \
            or args.mask is None \
            or args.defRouter is None \
            or args.dns is None \
            or args.domain is None \
            or args.lease is None:
        print(parser.usage)
        exit(0)

    # Create Dhcp Object
    dhcp = Dhcp(args.netIp, args.mask, args.defRouter, args.dns, args.domain, args.lease)
    if (dhcp.generate_dhcp_file()):
        print("Configuration Generated with sucess")
    else:
        print("Error while generating the file. Invalid parameters")


if __name__ == '__main__':
    main()
