# Subnetting - Usable Hosts
from subnet_mask_network import IPAddress
from subnet_network_address import network_address, default_prefix


def host_bits(c):
    return 32 - c


def subnet_bits(c, ip_address):
    prefix = default_prefix(ip_address)
    return c - prefix


def usable_hosts(c):  # Not including Network and Broadcast Address
    return (2 ** (32 - c)) - 2


def usable_subnets(c, ip_address):
    # If c < prefix -> Supernetting
    # If c > prefix -> Subnetting
    # If c = prefix -> Standard p -> Subnets = 1
    network = network_address(ip_address)
    prefix = default_prefix(ip_address)
    if c > prefix:
        return network, 2 ** (c - prefix)
    elif c == prefix:
        return network, 1
    else:
        raise ValueError(f"Supernetting: cannot calculate subnets (CIDR: /{c} < default /{prefix})")


def main():
    print("Networking: IPv4 Address, Subnet")
    n1, n2, n3, n4 = map(int, input("Enter IP Address numbers (n1, n2, n3, n4): ").split(","))
    c = int(input("Enter CIDR: "))
    ip_address = IPAddress(n1, n2, n3, n4, c)
    print(usable_subnets(c, ip_address)[0])
    print("- Number of Host bits:", host_bits(c))
    print("- Number of Subnet bits:", subnet_bits(c, ip_address))
    print("- Usable Hosts:", usable_hosts(c))
    print("- Usable Number of Subnets:", usable_subnets(c, ip_address)[1])
    print("- Network:", ip_address.Subnet[1])
    print("- Broadcast:", ip_address.Broadcast[1])
    print("- Range:", ip_address.ValidAddressesRange)


if __name__ == "__main__":
    main()
