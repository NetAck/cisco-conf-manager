import argparse


class EIGRP:
    def __init__(self, autonomous_system, networks, router_id, passive_interfaces):
        self.autonomous_system = autonomous_system
        self.networks = networks
        self.router_id = router_id
        self.passive_interfaces = passive_interfaces

    def generate_eigrp_file(self):
        string_eigrp = '! EIGRP Configurations\n' \
                      f'router eigrp {self.autonomous_system}\n' \
                      f'{generate_router_id(self.router_id)}\n' \
                      f'{generate_networks(self.networks)}' \
                      f'{generate_passive_interfaces(self.passive_interfaces)}' \
                      'exit'
        file = open('eigrp.txt', 'w')
        success = file.write(string_eigrp)
        file.close()
        return success


def main():
    parser = argparse.ArgumentParser()
    parser.usage = "eigrp -a <AS number> -r <router-id> -n <[net1, net2, ...]> -p <[g0/1, g0/2, ...]>"
    required = parser.add_argument_group('required arguments')
    required.add_argument('-a', '--autonomous-system', action='store', help='The autonomous of eigrp', required=True)
    parser.add_argument('-r', '--router-id', action='store', help='The id of ther router to eigrp', required=False)
    required.add_argument('-n', '--networks', action='store', nargs='*', help='List of networks', required=True)
    parser.add_argument('-p', '--passive-interface', action='store', nargs='*', help='List of Passive Interfaces', required=False)
    args = parser.parse_args()

    if args.networks is None or args.autonomous_system is None:
        print(parser.usage)
        exit(0)

    # Create eigrp object
    eigrp = EIGRP(args.autonomous_system, args.networks, args.router_id, args.passive_interface)
    if eigrp.generate_eigrp_file():
        print("Configuration Generated with sucess")
    else:
        print("Error while generating the file. Invalid parameters")


"""
Function to generate network commands for routing protocols
"""


def generate_networks(networks):
    str_nets = ''
    for net in networks:
        str_nets += f'network {net} 0.0.0.255\n'
    return str_nets


"""
Function to passive-interface commands for routing protocols
"""


def generate_passive_interfaces(passive_interfaces):
    str_pass_int = ''
    if passive_interfaces is None: return str_pass_int
    for interface in passive_interfaces:
        str_pass_int += f'passive-interface {interface}\n'
    return str_pass_int

'''
Function to generate router id command
'''
def generate_router_id(rid):
    return f'router-id {rid}' if rid is not None else ''


if __name__ == '__main__':
    main()
