from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
import os

# This is a standard simple connection using a dict for the connection info

password = getpass()

nxos1 = {
    "device_type":"cisco_nxos",
    "host":"host.domain.tld",
    "username":"user",
    "password":password,
    }


net_connect = ConnectHandler(**nxos1)

print(net_connect.find_prompt())
