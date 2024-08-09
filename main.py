import os
import time

def run_posix():
    from linux_methods import select_connection,select_config,set_dhcp,set_static
    while True:
        name = f"'{select_connection()}'"
        config = select_config()
        if config.address == "DHCP":
            print(f"Setting{name} to Auto(DHCP)...")
            set_dhcp(name)
        else:
            print(f"Setting{name} to {config}...")
            set_static(name,config.address, config.prefix, config.gateway)
        time.sleep(2)


def run_windows():
    from windows_methods import select_connection, select_config, set_dhcp
    while True:
        # name = select_connection()
        config = select_config()
        if config.address == "DHCP":
            print(f"Setting{name} to Auto(DHCP)...")
            set_dhcp(name)
        else:
            print(f"Setting{name} to {config}...")
            set_static(name,config.address, config.prefix, config.gateway)
        time.sleep(2)



if os.name == 'posix':
    print("POSIX")
    run_posix()

if os.name == 'nt':
    print("WINDOWS")
    run_windows()
