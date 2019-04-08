# execute_command.py
import duhs
import cat
def execute_command(command):
    command_data = command.split()
    main_command = command_data[0]
    args = command_data[1:]

    all_commands = {}
    all_commands['cat'] = lambda args : cat.cat(*args)
    all_commands['duhs'] = lambda args : duhs.duhs(*args)
    all_commands[main_command](args)

execute_command("duhs duhs.py")
execute_command("cat cat.py")
