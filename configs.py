class IP4Config:
    configs = []
    def __init__(self, address, prefix, gateway):
        self.address = address
        self.prefix = prefix
        self.gateway = gateway
        self.configs.append(self)
    def __repr__(self) -> str:
        return f"{self.address}/{self.prefix}, {self.gateway}"


auto = IP4Config("DHCP", "Auto", "Auto")
ten_dot = IP4Config("10.10.10.166", "24", "10.10.10.1")
one_nine_two = IP4Config("192.168.1.133", "24", "192.168.1.1")
self_assigned = IP4Config("169.254.1.1", "24", "169.254.1.1")

# print(IP4Config.configs)
