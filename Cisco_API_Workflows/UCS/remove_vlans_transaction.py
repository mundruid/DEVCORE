from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")

vlans = handle.query_classid("FabricVlan")

for vlan_mo in vlans:
    if vlan_mo.id != "1":
        handle.remove_mo(vlan_mo)

handle.commit()
