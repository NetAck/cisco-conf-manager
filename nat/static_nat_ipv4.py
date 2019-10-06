import argparse
import ipaddress



class Static_nat_ipv4:
    def __init__(self, inside_interface, local_ip, global_ip, outside_interface):
        self.inside_interface = inside_interface
        self.local_ip = ipaddress.IPv4Address(local_ip)
        self.global_ip = ipaddress.IPv4Address(global_ip)
        self.outside_interface = outside_interface

def generate_command(self):
    s = f"""\
        
ip nat inside source static {self.local_ip} {self.global_ip}
interface {self.inside_interface}
ip nat inside
exit
interface {self.outside_interface}
ip nat outside
exit\

    """
    return s

def append_to_file(self, filename = "static-nat-config.txt"):
    file = open(filename, "a")
    success = file.write(generate_command(self))
    file.close
    return success

        

def main():
    parser = argparse.ArgumentParser()
    parser.usage = 'Usage: python3 router.py ' + '-i <inside interface> -l <local ip address> -g <global ip address> -o <outside interface> -f <file to output>'
    required = parser.add_argument_group('required arguments')
    required.add_argument('-i', '--inside', action='store', type=str, help='specify the inside interface', required=True)
    required.add_argument('-l', '--local_ip', action='store', type=str, help='specify local ip address', required=True)
    required.add_argument('-g', '--global_ip', action='store', type=str, help='specify global ip address', required=True)
    required.add_argument('-o', '--outside', action='store', type=str, help='specify the outside interface', required=True)
    required.add_argument('-f', '--file', type=str, action='store', help='specify the file to generate/append', required=True)
    args = parser.parse_args()

    if args.inside is None \
            or args.local_ip is None \
            or args.global_ip is None \
            or args.outside is None:
        print(parser.usage)
        exit(0)

    # Create Static IPv4 Interface Object
    static_nat_ipv4 = Static_nat_ipv4(args.inside, args.local_ip, args.global_ip, args.outside)
    if (append_to_file(static_nat_ipv4, args.file)):
        print("Configuration Generated and Stored with sucess")
    else:
        print("Error while generating/appending the file. Invalid parameters")

if __name__ == '__main__':
    main()