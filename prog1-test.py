# Msizi Mthembu
# Adding a comment for Git
for vlan in vlans:
    id = vlan.get('id')
    name = vlan.get('name')
    print('\n)')
    print('CONFIGURING VLAN:' + id)
    commands = get_commands(id, name)
    for device in devices:
        push_commands(device, commands)
        print('\n')
print("Msizi made some changes")
