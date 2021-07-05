"""Use ucsmsdk to query objects and compute.
The UCS Object Model defines objects hierarchically;
the computeBlade and computeRackUnit objects are children
of the equipmentChassis object which is a child of the root
object topSystem.
"""

# Retrieve equipmentLocatorLed
from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.110", "ucspe", "ucspe")

compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(
            in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        print(compute_resource.dn, leds[0].oper_state)
