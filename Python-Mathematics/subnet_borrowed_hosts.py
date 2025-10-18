# Subnetting - Borrowed Hosts


def borrowed_bits(subnets):
    for i in range(1, subnets):
        if 2 ** i >= subnets:  # Break the loop when the i that
            # 2^i >= subnets is found
            return i


def usable_subnets(subnets, network):
    s = borrowed_bits(subnets)
    if network == 'A':
        prefix = 8
    elif network == 'B':
        prefix = 16
    else:
        prefix = 24

    cidr = prefix + s
    return cidr, 2 ** s, 2 ** (32 - cidr) - 2


def main():
    network = str(input("Enter Network Class: ").upper())
    if network not in ['A', 'B', 'C']:
        raise ValueError("Invalid Class for network, must be A, B, or C")

    subnets = int(input("Enter the number of subnets required: "))
    if subnets < 1:
        raise ValueError("Invalid Input for number of subnets as integer")

    print("Borrowed Bits:", borrowed_bits(subnets))
    print("CIDR:", usable_subnets(subnets, network)[0])
    print("Usable number of subnets:", usable_subnets(subnets, network)[1])
    print("Usable number of hosts for each subnet:", usable_subnets(subnets, network)[2])


if __name__ == "__main__":
    main()
