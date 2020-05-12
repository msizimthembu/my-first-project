# Msizi Mthembu
# Adding a comment for Git


>>>>>>> 71d529e6b703daf5d87b46c69d57369c3346dba1
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
