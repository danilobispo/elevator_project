from OrderList import OrderList


class Person(OrderList):
    """monitor the object"""
    _nid = -1
    _objectivefloor = -1
    _currentfloor = -1

    def __init__(self, nid, currentfloor):
        self._currentfloor = currentfloor
        self._nid = nid

    def callelevator(self, objectivefloor):
        self._objectivefloor = objectivefloor

    @property
    def currentfloor(self):
        return self._currentfloor

    @currentfloor.setter
    def currentfloor(self, newvalue):
        self._currentfloor = newvalue

    @property
    def objectivefloor(self):
        return self._currentfloor

    @objectivefloor.setter
    def objectivefloor(self, newvalue):
        self._objectivefloor = newvalue
        # if the objective floor has changed, then the elevator has to be notified
        self.notify()

