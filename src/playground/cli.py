# Provides access to command-line arguments
import sys as System

# Imports the Playground workspace manager
from .workspace import WorkSpace

# Imports terminal color constants
from .colors import Color


def main():
    if len(System.argv) == 1:
        print(Color.PRIMARY + " PlayGround Helper Tool " + Color.RESET)
        return

    command = System.argv[1]

    workspace = WorkSpace()

    if command == "seed":
        if workspace.is_seeded():
            print(Color.PRIMARY + "Already seeded." + Color.RESET)
            return
        else:
            workspace.seed()
            print(Color.PRIMARY + "Playground seeded." + Color.RESET)

    elif command == "configure":
        if workspace.is_seeded():
            pass
        else:
            print(Color.RED + "Playground has not been seeded." + Color.RESET)
            print(Color.PRIMARY + "Run playground seed first." + Color.RESET)