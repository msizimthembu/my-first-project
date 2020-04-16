""" Configuring VLANS """

def get_commands(vlan, name):
    commands = []
    commands.append('vlan ' + vlan)
    commands.append('name ' + name)

    return commands


def push_commands(device, commands):
    print("Connecting to device: {}".format(device))
    for cmd in commands:
        print("Sending command: {}".format(cmd))

devices = ['switch1', 'switch2', 'switch3']
vlans = [{'id': '10', 'name': 'USERS'}, 
         {'id': '20', 'name': 'DATA'}, 
         {'id': '30', 'name': 'WLAN'}]

         
