import sys
import json
import operator

class filter(object):
    def __init__(self,data={}):
        self.__data = data
        self.__sum = self.sum()
        self.__avrg = self.average()

    def sum(self):
        accumulate = 0.0
        for key, value in self.__data.iteritems():
            accumulate +=value
        return accumulate

    def average(self):
        count = len(self.__data.keys())
        if count==0 : return 0
        return self.sum()/count

    def large(self, bound, percent = False):
        result_set = dict()
        for key, value in self.__data.iteritems():
            if percent:
                value = value/ self.__sum
            if ( value >= bound):
                result_set[key] = value
        return result_set

    def small(self, bound, percent = True):
        result_set = dict()
        for key, value in self.__data.iteritems():
            if percent:
                value = value/ self.__sum
            if ( value<= bound):
                result_set[key] = value
        return result_set