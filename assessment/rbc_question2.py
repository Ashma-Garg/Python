command_string = input("Enter command: ")     # command should be like: UUUDUUDDUUU

initial_pos = 0
dict_command = {}
for i in command_string:
    dict_command[i] = dict_command.get(i, 0) + 1

if (dict_command.get('U', 0) > dict_command.get('D', 0)):
    print('U')
elif (dict_command.get('U', 0) < dict_command.get('D', 0)):
    print('D')
else:
    print("Initial Pos")