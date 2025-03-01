import json


with open("lab4\sample-data.json", "r") as file:
    data = json.load(file)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else ""
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(dn.ljust(50) + descr.ljust(20) + speed.ljust(10) + mtu)
