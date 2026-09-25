# Color Module
from .colors import Color

def writer( content : str , mode : str = "n") -> None:

    if mode == 'n' :
        print( Color.PRIMARY + content + Color.RESET )
    elif mode == 'c' :
        print( Color.RED + content + Color.RESET )