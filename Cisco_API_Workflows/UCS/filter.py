from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.10.20.113", "ucspe", "ucspe")
handle.login()

blades = handle.query_classid("computeBlade")
for blade in blades:
    print(blade.model, blade.serial, blade.dn,
          blade.total_memory, blade.num_of_cpus)

blades = handle.query_classid(
    "computeBlade", filter_str="(model, 'UCSB-EX-M4-1', type='eq')")
for blade in blades:
    print(blade.model, blade.serial, blade.dn,
          blade.total_memory, blade.num_of_cpus)
