from methods import *
import time

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
