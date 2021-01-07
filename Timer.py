import time

class Timer:
    def __init__(self):
        self.initialTime = time.perf_counter()

    def beginCounting(self):
        self.initialTime = time.perf_counter()

    def getTime(self):
        self.currentTime = time.perf_counter()
        return self.currentTime



#t = timer()
#t.getTime()
