import time

class timer:
    def __init__(self):
        self.initialTime = time.perf_counter()

    def beginConting(self):
        self.initialTime = time.perf_counter()

    def getTime(self):
        self.currentTime = time.perf_counter()
        return self.currentTime

#t = timer()
#t.getTime()
