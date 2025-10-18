# Network Address (Class A, B, C, ...)
from subnet_mask_network import IPAddress


def network_address(ip_address):
    # In Binary the first bits of n1 is 00 --> Class A
    if ip_address.n1 in range(1, 127 + 1):
        return "Network Class A"
    # In Binary the first bits of n1 is 10 --> Class B
    if ip_address.n1 in range(128, 191 + 1):
        return "Network Class B"
    # In Binary the first bits of n1 is 110 --> Class C
    if ip_address.n1 in range(192, 233 + 1):
        return "Network Class C"
    # In Binary the first bits of n1 is 1110 --> Class D
    if ip_address.n1 in range(234, 239 + 1):
        return "Network Class D (Multicast)"
    # In Binary the first bits of n1 is 1111 --> Class E
    if ip_address.n1 in range(240, 255 + 1):
        return "Network Class E (Experimental)"


def default_prefix(ip_address):
    network = network_address(ip_address)
    if network == "Network Class A":
        prefix = 8
        return prefix
    if network == "Network Class B":
        prefix = 16
        return prefix
    if network == "Network Class C":
        prefix = 24
        return prefix
    else:
        return None


def main():
    print("Networking: IPv4 Address, Subnet")
    n1, n2, n3, n4 = map(int, input("Enter IP Address numbers (n1, n2, n3, n4): ").split(","))
    c = int(input("Enter CIDR: "))
    ip_address = IPAddress(n1, n2, n3, n4, c)
    print(ip_address.Host)
    print(network_address(ip_address))
    print("Prefix:", default_prefix(ip_address))


if __name__ == "__main__":
    main()
