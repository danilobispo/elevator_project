
class Elevator:
    """Updates the Order Viewer and also implements the elevator priority """

    def update(self, person):
        print('Debugger: Person id #%d has objectivefloor %d and currentfloor %d' % (person.nid,
              person.objectivefloor, person.currentfloor))
