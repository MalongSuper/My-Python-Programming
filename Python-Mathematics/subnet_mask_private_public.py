# Determine Public Address or Private Address
from subnet_mask_network import IPAddress


class ExtendedAddress(IPAddress):
    @property
    def IsPrivate(self):
        if self.n1 == 10:
            return True
        elif self.n1 == 172 and self.n2 in range(16, 31 + 1):
            return True
        elif self.n1 == 192 and self.n2 == 168:
            return True
        return False

    @property
    def IPType(self):
        return "Private IP" if self.IsPrivate else "Public IP"


def main():
    n1, n2, n3, n4 = map(int, input("Enter IP Address numbers (n1, n2, n3, n4): ").split(","))
    c = int(input("Enter CIDR: "))
    ip_address = ExtendedAddress(n1, n2, n3, n4, c)
    print(ip_address.IPType)


if __name__ == "__main__":
    main()
