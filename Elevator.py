from Timer import Timer
import random


class Elevator:
    __instance = None

    _pathFloors = []  # lista de andares
    _askedFloors = []
    _currentFloor: int
    _currentState = False  # stopped = false; moving = true
    _timer = Timer()

    # Gets and setters

    @property
    def pathFloors(self):
        return self._pathFloors

    @pathFloors.setter
    def pathFloors(self, newvalue):
        if newvalue < 1 | newvalue > 10:
            raise ValueError("Invalid floor, please try again")
        self._pathFloors = newvalue

    @property
    def askedFloors(self):
        return self._askedFloors

    @askedFloors.setter
    def askedFloors(self, newvalue):
        if newvalue < 1 | newvalue > 10:
            raise ValueError("Invalid floor, please try again")
        self._askedFloors = newvalue

    @property
    def currentFloor(self):
        return self._currentFloor

    @currentFloor.setter
    def currentFloor(self, newvalue):
        if newvalue < 1 | newvalue > 10:
            raise ValueError("Invalid floor, please try again")
        self._currentFloor = newvalue

    @property
    def currentState(self):
        return self._currentState

    @currentState.setter
    def currentState(self, newvalue):
        if newvalue == self._currentState:
            raise ValueError("This is already the current state of the elevator")
        elif newvalue != False | newvalue != True:
            raise ValueError("Invalid value for state")
        self._currentState = newvalue

    # Singleton access method
    @staticmethod
    def getInstance():
        """ Static access method. """
        if Elevator.__instance is None:
            Elevator(1)
        return Elevator.__instance

    def __init__(self, currentFloor):
        self._pathFloors = []  # lista de andares
        self._askedFloors = []
        self._currentFloor = currentFloor
        self._currentState = False  # stopped = false; moving = true
        self._timer = Timer()

        if Elevator.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Elevator.__instance = self

    def update(self, person):
        print('Debugger: Person id #%d has objectivefloor %d and currentfloor %d' % (person.nid,
                                                                                     person.objectivefloor,
                                                                                     person.currentfloor))

    # undone
    def arrival(self):
        if len(self._pathFloors) > 0:
            if self._currentFloor == self._pathFloors[0]:
                self._pathFloors.pop(0)

    def setOffset(self, time):
        """An added time in the timer object when it reaches an asked floor, simulating the time it takes for
        a person to enter or exit the elevator"""
        return time + random.randrange(1, 4, 1)

    def newRequest(self, floor):
        self._askedFloors.append(floor)
        print("self.askedFloors " + str(self._askedFloors))
        # print("path before reorganize " + str(self._pathFloors))
        self.reorganizePath()
        # print("path after reorganize " + str(self._pathFloors))

        self.start_trip()

    def reorganizePath(self):
        i = 0

        # if there isn't a floor on the path
        if len(self._pathFloors) == 0:
            self._pathFloors.append(self._askedFloors[0])
            self._askedFloors.remove(self._askedFloors[len(self._askedFloors) - 1])  # remove the last element

        else:
            # is the elevator going down?
            if self._currentFloor > self._pathFloors[0]:
                # is the new floor on the way?
                if self._currentFloor > self._askedFloors[len(self._askedFloors) - 1]:
                    self._pathFloors.append(self._askedFloors[len(self._askedFloors) - 1])
                    self._askedFloors.remove(self._askedFloors[len(self._askedFloors) - 1])  # remove the last element
                    # top down
                    self._pathFloors.sort(reverse=True)

            # is the elevator going up?
            elif self._currentFloor < self._pathFloors[0]:
                # is the new floor on the way?
                if self._currentFloor < self._askedFloors[i]:
                    print("is it?")
                    self._pathFloors.append(self._askedFloors[len(self._askedFloors) - 1])
                    self._askedFloors.remove(self._askedFloors[len(self._askedFloors) - 1])  # remove the last element
                    self._pathFloors.sort(reverse=False)
        list(self._pathFloors)

    def start_trip(self):
        """Starts trip when the askedfloor list is not empty"""
        if len(self._pathFloors) > 0:
            if self.currentFloor != self._pathFloors[0]:
                self._timer.beginCounting()
                initial_time = self._timer.initialTime
                trip_time = self._timer.initialTime  # trip time begins with the initial time and is incremented after
                # Elevator is now moving
                print("Elevator will begin the trip, the current floor is: ", self._currentFloor)
                print("The objective floor is: ", self._pathFloors[0])
                print("The current start time of the trip is: ", trip_time)
                self._currentState = True

                while self._currentFloor != self._pathFloors[0]:
                    down_or_up = self.determine_elevator_direction()



                    if self._timer.getTime() >= trip_time + 1:
                        if not down_or_up:  # Going down
                            self._currentFloor -= 1
                            print("Elevator's current floor: ", self._currentFloor)
                        else:  # Going up
                            self._currentFloor += 1
                            print("Elevator's current floor: ", self._currentFloor)
                        trip_time += 1
                        print("Trip current time:", trip_time)
                        print("Timer time:", self._timer.getTime())
                        print("Elevator is going", "up" if down_or_up else "down")
                        distance = self.determineelevatordistance()  # Determine the distance
                        print("Distance: ", distance)



                if self._currentFloor == self._pathFloors[0]:
                    # Elevator has stopped at the destination
                    self._currentState = False
                    # The person is getting out, so a little more time is added
                    trip_time = self.setOffset(trip_time)
                    trip_time = trip_time - initial_time
                    print("Elevator's final floor: ", self._currentFloor)
                    print("Total time elapsed:", trip_time)
                    self.arrival()
            else:
                print("The elevator is already in the requested floor!")

    def determine_elevator_direction(self):
        """False for going down and True for going Up"""
        return False if self._currentFloor > self._pathFloors[0] else True

    def determineelevatordistance(self):
        """Returns the distance from current floor to objective floor"""
        return abs(self._currentFloor - self._pathFloors[0])
