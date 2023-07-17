"""Prints a list of all switches to console, for reference."""
from jns_cisco_devices import cisco_devices

buildings = cisco_devices.interface_buildings()

for building in buildings:
    for switch in building:
        print(switch)
