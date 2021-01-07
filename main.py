# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Elevator import Elevator

import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_personlist(personlist):
    for i in personlist:
        print("nid:", i.nid)
        print("currentfloor:", i.currentfloor)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    e = Elevator(3)
    e.newRequest(2)
    e.newRequest(4)
    e.newRequest(5)
    e.newRequest(1)
    e.newRequest(3)
    e.newRequest(6)
    e.newRequest(4)
    e.newRequest(5)
    e.newRequest(9)
    e.newRequest(10)
    e.newRequest(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
