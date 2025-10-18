# Subnetting Mask Address
from subnetting_network import subnetting
from ipaddress import IPv4Network


def main():
    print("Network: Subnetting IP Address")
    n1, n2, n3, n4 = map(int, input("Enter IP Address numbers (n1, n2, n3, n4): ").split(","))
    c = int(input("Enter CIDR: "))
    network = IPv4Network(f"{n1}.{n2}.{n3}.{n4}/{c}", strict=False)
    subnets = int(input("Enter number of subnets: "))
    hosts = {}
    for i in range(subnets):
        sub_address = int(input(f"Subnet {i} - Enter the number of hosts: "))
        hosts[f'Subnet {i}'] = sub_address

    print("Result:")
    subnetting(network, hosts)


if __name__ == "__main__":
    main()
