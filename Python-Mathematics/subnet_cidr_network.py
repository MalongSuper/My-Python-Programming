# Table of CIDR Network
from subnet_mask_network import IPAddress


def main():
    print("{:<6} {:<40} {:<15}".format("CIDR", "Binary", "Decimal"))
    print("-" * 60)
    for c in range(1, 32 + 1):
        ipaddress = IPAddress(1, 1, 1, 1, c)
        print("{:<6} {:<40} {:<15}".format(f"/{c}", ipaddress.Mask[0], ipaddress.Mask[1]))


if __name__ == "__main__":
    main()
