import subprocess
from configs import *
import psutil


def active_connections():
    connections = []
    interfaces = psutil.net_if_addrs()
    for interface, info in interfaces.items():
        if interface.startswith("Local Area Connection"):
            continue
        if interface.startswith("Loopback"):
            continue
        if interface.startswith("Bluetooth"):
            pass
        else:
            # pass
            address = info[1].address
            netmask = info[1].netmask
            connections.append((interface, address, netmask))
    return connections


def select_connection():
    connections = active_connections()
    for index, connection in enumerate(connections):
        print(f"{index}: {connection[0]} {connection[1]}, {connection[2]}")
    selection = input("Select a connection: ")
    connection = connections[int(selection)]
    print(connection)
    return connection[0]


def select_config():
    for index, config in enumerate(IP4Config.configs):
        print(f"{index}: {config}")

    while True:
        selection = input("Select a config: ")
        if int(selection) not in range(len(IP4Config.configs)):
            print("Not valid")
        else:
            config = (IP4Config.configs[int(selection)])
            print(config)
            return config


def set_dhcp(interface):
    commands = [
        f"nmcli con mod {interface} ipv4.dns-options auto",
        f"nmcli con mod {interface} ipv4.method auto",
        f"nmcli con up {interface}",
    ]
    for command in commands:
        result = subprocess.run(command, shell=True, check=True, capture_output=True)
        message = str(result.stdout)
        success = "success"
        if len(message) > 0 and success in message:
            print("Success")


def set_static(interface, address, prefix, gateway):
    commands = [
        netsh interface ip set address name=interface address netmask gateway
    ]
    for command in commands:
        result = subprocess.run(command, shell=True, check=True, capture_output=True)
        message = str(result.stdout)
        success = "success"
        if len(message) > 0 and success in message:
            print("Success")
