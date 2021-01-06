from Timer import Timer

class Elevator:
    """Updates the Order Viewer and also implements the elevator priority """
    def __init__(self, currentFloor):
        self.pathFloors = [] #lista de andares
        self.askedFloors = []
        self.currentFloor = currentFloor
        self.currentState = False #stopped = false; moving = true
        self.timer = Timer()

    def update(self, person):
        print('Debugger: Person id #%d has objectivefloor %d and currentfloor %d' % (person.nid,
              person.objectivefloor, person.currentfloor))

    def showTime(self):
        #print(self.timer.getTime())
        print("nada")

    #undone
    def arrival(self):
        if len(self.pathFloors)>0:
            if self.currentFloor == self.pathFloors[0]:
                self.pathFloors.pop(0)

    def newRequest(self, floor):
        self.askedFloors.append(floor)
        #print("self.askedFloors " + str(self.askedFloors))
        #print("path before reorganize " + str(self.pathFloors))
        self.reorganizePath()
        #print("path after reorganize " + str(self.pathFloors))

    def reorganizePath(self):
        i = 0

        #if there isn't a floor on the path
        if len(self.pathFloors)==0:
            self.pathFloors.append(self.askedFloors[0])
            self.askedFloors.remove(self.askedFloors[len(self.askedFloors) - 1])  # remove the last element

        else:
            # is the elevator going down?
            if self.currentFloor>self.pathFloors[0]:
                #is the new floor on the way?
                if self.currentFloor>self.askedFloors[len(self.askedFloors)-1]:
                    self.pathFloors.append(self.askedFloors[len(self.askedFloors)-1])
                    self.askedFloors.remove(self.askedFloors[len(self.askedFloors) - 1])  # remove the last element
                    #top down
                    self.pathFloors.sort(reverse=True)

            #is the elevator going up?
            elif self.currentFloor<self.pathFloors[0]:
                #is the new floor on the way?
                if self.currentFloor<self.askedFloors[i]:
                    print("is it?")
                    self.pathFloors.append(self.askedFloors[len(self.askedFloors) - 1])
                    self.askedFloors.remove(self.askedFloors[len(self.askedFloors) - 1])  # remove the last element
                    self.pathFloors.sort(reverse=False)
        list(self.pathFloors)


#e=Elevator(3)

#e.arrival()
#e.newRequest(2)
#e.arrival()
#e.newRequest(4)
#e.arrival()
#e.newRequest(5)
#e.arrival()
#e.newRequest(1)
#e.arrival()
