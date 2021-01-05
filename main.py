# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Elevator import Elevator
from Person import Person

import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_personlist(personlist):
    for i in personlist:
        print("nid:", i._nid)
        print("currentfloor:", i._currentfloor)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    elevator = Elevator()
    personlist = []
    for i in range(0, 10):
        personlist.append(Person(i, random.randrange(1, 10, 1)))
    print_personlist(personlist)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
