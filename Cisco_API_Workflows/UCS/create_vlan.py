from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan
from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")

# get parent vlan
lan_cloud = handle.query_classid("FabricLanCloud")
# create new vlan
vlan_mo = FabricVlan(parent_mo_or_dn=lan_cloud[0], name="vlan0", id="100")
# add vlan, second argument indicates modify_present: update object if it already exists
handle.add_mo(vlan_mo, True)
handle.commit()
