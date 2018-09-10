from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand

class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = 'UpdateQuantity'
    description = 'UpdateQuantity number'

    def __init__(self, args):
        self.newqty = args[1]

    def execute(self):
        print("updated order command, the quality is now {}".format(self.newqty))
