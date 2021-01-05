

class Elevator:
    """Updates the Order Viewer and also implements the elevator priority """

    def update(self, order):
        print('Debugger: Person {%d} has objectivefloor %d and currentfloor %d', order.objectivefloor,
              order.currentfloor)