# Subnet Mask in Networking
# Determine IPv4 Address


class IPAddress:
    def __init__(self, n1, n2, n3, n4, c):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.c = c
        if n1 > 255 or n1 < 0:
            raise ValueError("Invalid value for n1: must be within 0 and 255")
        if n2 > 255 or n2 < 0:
            raise ValueError("Invalid value for n2: must be within 0 and 255")
        if n3 > 255 or n3 < 0:
            raise ValueError("Invalid value for n3: must be within 0 and 255")
        if n4 > 255 or n4 < 0:
            raise ValueError("Invalid value for n4: must be within 0 and 255")
        if c < 0 or c > 32:
            raise ValueError("Invalid value for CIDR Notation: must be within 0 and 32")

    def __str__(self):
        return f"{self.n1}.{self.n2}.{self.n3}.{self.n4}/{self.c}"

    @property
    def Address(self):
        return IPAddress.__str__(self)

    @property
    def Host(self):
        host = [self.n1, self.n2, self.n3, self.n4]
        host_bin = [bin(h)[2:] for h in host]  # Convert to binary
        # if the binary is less than 8 digits, add 0 before it
        for i in range(len(host_bin)):
            if len(host_bin[i]) < 8:
                # use zfill(8) for fill 8 bits
                host_bin[i] = host_bin[i].zfill(8)
        return ' '.join(host_bin), '.'.join(map(str, host))

    @property
    def HostBinary(self):
        return self.Host[0]

    @property
    def HostDecimal(self):
        return self.Host[1]

    @property
    def Mask(self):  # Subnet Mask
        mask_list = "00000000000000000000000000000000"
        mask_list = list(mask_list)
        binary, decimal = [], []
        for i in range(self.c):
            # Replace the mask_list to 1 based on the CIDR
            # When CIDR = /n, there are 'n' number of 1s, the rest are 0s
            mask_list[i] = "1"
        # Join the list to string
        mask_list = ''.join(mask_list)
        for j in range(0, len(mask_list), 8):
            bina = str(mask_list[j:j + 8])  # Get every eight numbers
            dec = int(bina, 2)  # Binary to decimal
            binary.append(bina)
            decimal.append(dec)
        # Return the element
        return ' '.join(binary), '.'.join(map(str, decimal))

    @property
    def MaskBinary(self):
        return self.Mask[0]

    @property
    def MaskDecimal(self):
        return self.Mask[1]

    @property
    def Subnet(self):  # Network ID
        subnet_list = []
        binary, decimal = [], []  # The final result
        host_bin, mask_bin = self.Host[0], self.Mask[0]
        for i in range(len(host_bin)):
            # Use bitwise AND
            # If 0 AND 0 —> 0
            # If (0 AND 1) or (1 AND 0) —> 0
            # If 1 AND 1 —> 1
            if host_bin[i] == mask_bin[i] == "1":
                subnet_list.append("1")
            elif host_bin[i] == mask_bin[i] == "0":
                subnet_list.append("0")
            elif ((host_bin[i] == "0" and mask_bin[i] == "1")
                  or (host_bin[i] == "1" and mask_bin[i] == "0")):
                subnet_list.append("0")
        # Join the list to string
        subnet_list = ''.join(subnet_list)
        for j in range(0, len(subnet_list), 8):
            bina = str(subnet_list[j:j + 8])  # Get every eight numbers
            dec = int(bina, 2)  # Binary to decimal
            binary.append(bina)
            decimal.append(dec)
        return ' '.join(binary), '.'.join(map(str, decimal))

    @property
    def SubnetBinary(self):
        return self.Subnet[0]

    @property
    def SubnetDecimal(self):
        return self.Subnet[1]

    @property
    def Broadcast(self):  # Broadcast ID
        broadcast_list = []
        subnet = self.Subnet[0]
        mask = self.Mask[0]
        binary, decimal = [], []  # The final result
        # Make it a string, then convert it to list
        mask = list(''.join(mask))
        for i in range(len(mask)):
            # Swap 0 to 1, 1 to 0, invert Subnet Mask
            if mask[i] == '0':
                mask[i] = '1'
            elif mask[i] == '1':
                mask[i] = '0'
        invert_mask = ''.join(mask)
        for i in range(len(invert_mask)):
            # Use Bitwise OR
            # If 0 OR 0 —> 0
            # If (0 OR 1) or (1 OR 0) —> 1
            # If 1 OR 1 —> 1
            if invert_mask[i] == subnet[i] == "1":
                broadcast_list.append("1")
            elif invert_mask[i] == subnet[i] == "0":
                broadcast_list.append("0")
            elif ((invert_mask[i] == "0" or subnet[i] == "1")
                  or (invert_mask[i] == "1" or subnet[i] == "0")):
                broadcast_list.append("1")
        # Convert to decimal
        broadcast_list = ''.join(broadcast_list)
        for j in range(0, len(broadcast_list), 8):
            bina = str(broadcast_list[j:j + 8])  # Get every eight numbers
            dec = int(bina, 2)  # Binary to decimal
            binary.append(bina)
            decimal.append(dec)
        # Return the element
        return ' '.join(binary), '.'.join(map(str, decimal))

    @property
    def BroadcastBinary(self):
        return self.Broadcast[0]

    @property
    def BroadcastDecimal(self):
        return self.Broadcast[1]

    @property
    def First(self):  # The first IP Address
        subnet_bin, subnet_dec = self.Subnet[0], self.Subnet[1]
        binary, decimal = list(subnet_bin), list(subnet_dec)
        decimal[-1] = str(int(decimal[-1]) + 1)
        binary[-1] = str(int(binary[-1]) + 1)
        return ''.join(binary), ''.join(decimal)

    @property
    def FirstBinary(self):
        return self.First[0]

    @property
    def FirstDecimal(self):
        return self.First[1]

    @property
    def Last(self):
        broad_bin, broad_dec = self.Broadcast[0], self.Broadcast[1]
        binary, decimal = list(broad_bin), list(broad_dec)
        decimal[-1] = str(int(decimal[-1]) - 1)
        binary[-1] = str(int(binary[-1]) - 1)
        return ''.join(binary), ''.join(decimal)

    @property
    def LastBinary(self):
        return self.Last[0]

    @property
    def LastDecimal(self):
        return self.Last[1]

    @property
    def ValidAddresses(self):  # Calculate the number of valid IP Addresses
        # H = 32 - given CIDR
        # then 2^H - 2 will give us the maximum number of IP Addresses
        # Subtract 2 to exclude the network ID and broadcast ID
        # They cannot be used as the ID addresses of the devices
        host_bits = 32 - self.c
        return f"Number of valid IP addresses: {(2 ** host_bits) - 2}"

    @property
    def ValidAddressesRange(self):  # Return the decimal of First and Last
        # as the range of valid IP address
        return f"[First: {self.First[1]}, Last: {self.Last[1]}]"


def main():
    print("Networking: IPv4 Address, Subnet")
    n1, n2, n3, n4 = map(int, input("Enter IP Address numbers (n1, n2, n3, n4): ").split(","))
    c = int(input("Enter CIDR: "))
    ip_address = IPAddress(n1, n2, n3, n4, c)  # Create IPAddress instance
    print("IP Address:", ip_address.Address)
    print("Host:", ip_address.Host)
    print("Mask:", ip_address.Mask)
    print("Subnet:", ip_address.Subnet)
    print("First:", ip_address.First)
    print("Last:", ip_address.Last)
    print("Broadcast:", ip_address.Broadcast)
    print(ip_address.ValidAddresses)
    print(ip_address.ValidAddressesRange)


if __name__ == "__main__":
    main()
