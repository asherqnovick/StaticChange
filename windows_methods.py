import subprocess
from configs import *

def active_connections():
    client = NM.Client.new(None)
    active_connections = client.get_active_connections()
    connections = []
    for connection in active_connections:
        # if connection.get_id() != "lo":
        name = connection.get_id()
        interface = (connection.get_devices()[0].get_iface())
        address = connection.get_ip4_config().get_addresses()[0].get_address()
        prefix = connection.get_ip4_config().get_addresses()[0].get_prefix()
        gateway = connection.get_ip4_config().get_gateway()
        mode = dir(connection.get_ip4_config())
        connections.append((name, interface, address, prefix, gateway))
    return connections


def select_connection():
    connections = active_connections()
    for index, connection in enumerate(connections):
        if connection[0] != "lo":
            print(f"{index}: {connection[1]}, {connection[0]}, {connection[2]}")
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
        f"nmcli con mod {interface} ipv4.addresses {address}/{prefix}",
        f"nmcli con mod {interface} ipv4.gateway {gateway}",
        f"nmcli con mod {interface} ipv4.dns 1.1.1.1",
        f"nmcli con mod {interface} ipv4.method manual",
        f"nmcli con up {interface}",
    ]
    for command in commands:
        result = subprocess.run(command, shell=True, check=True, capture_output=True)
        message = str(result.stdout)
        success = "success"
        if len(message) > 0 and success in message:
            print("Success")
