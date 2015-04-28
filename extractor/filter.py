import sys
import json
import operator
import numpy as np

class filter(object):
    def __init__(self,data={}):
        self.__data = data
        self.__sum = self.sum()
        self.__avrg = self.average()
        self.__std = np.std(data.values())

    def sum(self):
        accumulate = 0.0
        for key, value in self.__data.iteritems():
            accumulate +=value
        return accumulate

    def average(self):
        count = len(self.__data.keys())
        if count==0 : return 0
        return self.sum()/count

    def large(self, delta=1, percent = False):
        result_set = dict()
        for key, value in self.__data.iteritems():
            if percent:
                value = value/ self.__sum
            if ( value >= (delta*self.__std+self.__avrg)):
                result_set[key] = value
        return result_set

    def small(self, delta=1, percent = False):
        result_set = dict()
        for key, value in self.__data.iteritems():
            if percent:
                value = value/ self.__sum
            if ( value<= (self.__avrg - delta*self.__std)):
                result_set[key] = value
        return result_set