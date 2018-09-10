from update_order import UpdateOrder

def get_commands():
  commands = [UpdateOrder]
  return dict([cls.name, cls] for cls in commands)

print(get_commands())

commands = get_commands()
command = commands['UpdateQuantity']
command.execute();