from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")
lan_cloud = handle.query_classid("FabricLanCloud")
vlans_before = handle.query_classid("FabricVlan")
for vlan in vlans_before:
    print(f"Vlans before {vlan}")

vlans = ["200", "201", "202"]

for vlan in vlans:
    vlan_mo = FabricVlan(
        parent_mo_or_dn=lan_cloud[0], name="vlan"+vlan, id=vlan)
    handle.add_mo(vlan_mo)

handle.commit()
vlans_after = handle.query_classid("FabricVlan")
for vlan in vlans_after:
    print(f"Vlans after {vlan}")
