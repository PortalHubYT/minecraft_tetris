from mc_api.components.BlockHandler import BlockHandler
from mc_api.components import CustomFunction, Block, BlockCoordinates

class SetBlock(CustomFunction):

    def __init__(self, block_coordinates: BlockCoordinates, block: Block):
        self.check_interface()

        self.block_coordinates = self.format_arg(block_coordinates, BlockCoordinates)
        self.block = self.format_arg(block, Block)
    
        self.response = self.send('setblock', self.block_coordinates, self.block)
        self.status = self.execute_check(self.response)

        if self.status is str:
            self.unexpected_status(__file__, self.status, self.command)


def set_block(block_coordinates: BlockCoordinates or tuple, 
                block: Block or str,
                block_handler=BlockHandler or str,
                block_handler_option=Block or str) -> bool:

    command = SetBlock(block_coordinates, block)
    return command.status

class UnexpectedReturn(Exception):
    pass