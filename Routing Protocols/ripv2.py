import argparse


class Ripv2:
    def __init__(self, version, summarization, networks, passive_interfaces):
        self.version = version
        self.summarization = summarization
        self.networks = networks
        self.passive_interfaces = passive_interfaces

    def generate_ripv2_file(self):
        string_ripv2 = '! RIPV2 Configurations\n' \
                      'router rip\n' \
                      f'version {self.version}\n' \
                      f'{self.summarization}autosummary\n' \
                      f'{generate_networks(self.networks)}' \
                      f'{generate_passive_interfaces(self.passive_interfaces)}' \
                      'exit'
        file = open('ripv2.txt', 'w')
        success = file.write(string_ripv2)
        file.close()
        return success


def main():
    parser = argparse.ArgumentParser()
    parser.usage = "ripv2 -s -n <[net1, net2, ...]> -p <[g0/1, g0/2, ...]>"
    required = parser.add_argument_group('required arguments')
    parser.add_argument('-s', '--summarization', action='store_true', help='If presents activate the summarization',
                        required=False)
    required.add_argument('-n', '--networks', action='store', nargs='*', help='List of networks', required=True)
    parser.add_argument('-p', '--passive-interface', action='store', nargs='*', help='List of Passive Interfaces',
                        required=False)
    args = parser.parse_args()

    if args.networks is None:
        print(parser.usage)
        exit(0)

    # Create ripv2 object
    str_sum = '' if args.summarization else 'no'
    ripv2 = Ripv2('2', str_sum, args.networks, args.passive_interface)
    if ripv2.generate_ripv2_file():
        print("Configuration Generated with sucess")
    else:
        print("Error while generating the file. Invalid parameters")


"""
Function to generate network commands for routing protocols
"""


def generate_networks(networks):
    str_nets = ''
    for net in networks:
        str_nets += f'network {net}\n'
    return str_nets


"""
Function to passive-interface commands for routing protocols
"""


def generate_passive_interfaces(passive_interfaces):
    str_pass_int = ''
    if passive_interfaces is None: return str_pass_int;
    for interface in passive_interfaces:
        str_pass_int += f'passive-interface {interface}\n'
    return str_pass_int


if __name__ == '__main__':
    main()
