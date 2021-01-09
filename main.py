# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Elevator import Elevator
import time
import threading

import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_personlist(personlist):
    for i in personlist:
        print("nid:", i.nid)
        print("currentfloor:", i.currentfloor)

def testRequest(e):
    time.sleep(0.2)
    e.newRequest(2)
    time.sleep(1)
    e.newRequest(4)
    time.sleep(0.1)
    e.newRequest(5)
    time.sleep(0.5)
    e.newRequest(1)
    time.sleep(0.1)
    e.newRequest(3)
    e.newRequest(6)
    time.sleep(0.2)
    e.newRequest(4)
    e.newRequest(5)
    e.newRequest(9)
    time.sleep(1)
    e.newRequest(10)
    e.newRequest(10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')

    e = Elevator(3)

    t=threading.Thread(target=testRequest, args=(e,))
    t.start()

    while True:
        e.start_trip()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
