from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")

compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

for compute_resource_class in compute_resources:
    for compute_resource in compute_resources[compute_resource_class]:
        leds = handle.query_children(
            in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        previous_oper_state = leds[0].oper_state

        if leds[0].oper_state == "on":
            leds[0].admin_state = "off"
        else:
            leds[0].admin_state = "on"

        handle.set_mo(leds[0])
        handle.commit()
        print("dn:", compute_resource.dn,
              "led previous", previous_oper_state,
              "led current", leds[0].admin_state)
