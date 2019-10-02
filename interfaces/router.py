import ipaddress

class static_ipv4:
    def __init__(self, interface, description, ip,  shutdown, mask = "0"):
        self.interface = interface
        self.description = description
        self.ip_address = ipaddress.ip_address(ip)
        if mask == 0:
            a = ipaddress.ip_network(ip).with_netmask.split('/')
            mask = a[1]
        self.mask = mask
        self.shutdown = shutdown

        def generate_command():
            s = f"""\
            enable
            configure terminal
            interface {check_interface}
            description {check_description}
            ip address {check_ip} {check_mask}
            {check_shutdown} shutdown
            exit\
            """
            return s
        

        def check_shutdown():
            if (self.shutdown == 1):
                return "no "
            return ""

        def check_description():
            if(description == ""):
                return ""
            return "description %s" % (self.description)

        def check_ip():
            return self.ip_address
        
        def check_mask():
            return self.mask

        def check_interface():
            return self.interface

        def append_to_file(filename):
            file = open(filename, "a")
            success = file.write(generate_command)
            file.close
            return success