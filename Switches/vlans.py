import argparse


class Vlan:
    def __init__(self, vlan_number, vlan_name):
        self.vlan_number = vlan_number
        self.vlan_name = vlan_name

    def generate_vlan_file(self):
        string_vlan = self.generate_vlan_string()
        file = open('vlans.txt', 'w')
        success = file.write(string_vlan)
        file.close()
        return success

    def generate_vlan_string(self):
        str = f'vlan {self.vlan_number}'
        if self.vlan_name is not None:
            str += f'\nname {self.vlan_name}'
        return str


def main():
    parser = argparse.ArgumentParser();
    parser.usage = "vlans.py -n <vlan_number> -N <vlan_name>"
    required = parser.add_argument_group('required arguments')
    required.add_argument('-n', '--vlan-number', action='store', help='The number of vlan',
                        required=True)
    parser.add_argument('-N', '--vlan-name', action='store', help='The name of the vlan',
                        required=False)

    args = parser.parse_args()

    if args.vlan_number is None:
        print(parser.usage)
        exit(0)

    # Create vlan object
    vlan = Vlan(args.vlan_number, args.vlan_name)
    if vlan.generate_vlan_file():
        print("Configuration Generated with sucess")
    else:
        print("Error while generating the file. Invalid parameters")


if __name__ == '__main__':
    main()