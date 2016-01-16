import os
from EMart import *

def main():
    """Deletes .pyc files and runs the program.

    """

    # Opens file directory
    directory = os.listdir('.')
    for filename in directory:
        # Delete pyc memory files
        if filename[-3:] == 'pyc':
            os.remove(filename)

    # Create GUI instance, open program window
    openwindow = GUI()

main()