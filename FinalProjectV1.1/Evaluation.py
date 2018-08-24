import time
import numpy as np



class Evaluations(object):
    def __init__(self):
        self.record_list = []

    def time_caculation1(self):
        self.start = time.time()
        # print (self.start)

    def time_caculation2(self):
        self.end = time.time()
        self.record_list.append(self.end - self.start)
        # print (self.end)
        print(self.end - self.start)
        print(self.record_list)
        np.savetxt('RunningTime.csv', self.record_list, delimiter=',')
