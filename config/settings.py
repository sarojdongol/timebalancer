from typing import Tuple

class Setting():
    """
    Generate Tuple Config
    """
    def __init__(self,width: int, height: int) -> Tuple:
        self.width = width
        self.height = height
    
    def setter():
        pass

    def get_config(self):
        return (self.width,self.height)