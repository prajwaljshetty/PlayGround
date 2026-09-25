# Provides access to command-line arguments
import sys as System

# Imports the Playground workspace manager
from .workspace import WorkSpace

# Writer Module
from .writer import writer


def main():
    if len(System.argv) == 1:
        writer(" PlayGround Helper Tool ")
        return 0

    command = System.argv[1]

    workspace = WorkSpace()

    if command == "seed":
        if workspace.is_seeded():
            writer("Already seeded")
            return 0
        else:
            workspace.seed()
            writer("Playground seeded.")

    elif command == "configure":
        if workspace.is_seeded():
            pass
        else:
            writer("Playground has not been seeded.","c")
            writer("Run playground seed first.")
