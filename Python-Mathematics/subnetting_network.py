# Network of IP Addresses - Subnetting
from ipaddress import IPv4Network
from math import log2


def get_required_hosts(hosts):
    # Minimum Hosts required: [2^2, 2^3, 2^4, ...]
    available_hosts = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
    required_hosts = []
    # Get the required hosts
    for host in hosts.values():
        for available in available_hosts:
            # Break the loop if the available_hosts greater than
            # the hosts is found
            if available > host:
                required_hosts.append(available)
                break
    return required_hosts


def get_cidr(required_hosts):
    return [32 - int(log2(hosts)) for hosts in required_hosts]


def subnetting(network, hosts):
    # Optional: Sort the subnets in descending order
    # Prioritize the one with the largest required hosts
    required_hosts = get_required_hosts(hosts)
    cidr = get_cidr(required_hosts)
    current_address = network.network_address
    for c, h in zip(cidr, hosts):
        # Set network address
        subnet = IPv4Network(f"{current_address}/{c}", strict=False)
        # get broadcast subnet
        network_addr = subnet.network_address
        broadcast_addr = subnet.network_address + (2 ** (32 - c) - 1)
        # usable Ips
        first_addr, last_addr = network_addr + 1, broadcast_addr - 1
        print(f"{h}: {first_addr} - {last_addr}")
        # Update the next address, 'last_addr + 2 to exclude the broadcast_addr
        # of the previous network, and the network_addr of the current network
        current_address = last_addr + 2


def main():
    print("+ Example 1")
    network = IPv4Network("192.168.10.0/24")
    hosts = {"Network A": 60, "Network B": 30,
             "Network C": 14, "Network D": 6}
    subnetting(network, hosts)
    print("+ Example 2")
    network = IPv4Network("172.16.0.0/20")
    hosts = {"Network A": 400, "Network B": 200,
             "Network C": 100, "Network D": 50,
             "Network E": 25}
    subnetting(network, hosts)


if __name__ == "__main__":
    main()
