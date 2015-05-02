import sys
from issuesPersonDetector import large_author, small_author
from commitsPersonDetector import large_commiter,small_commiter

#compare if somebody made both most/smallest commits and issues

leaders= dict()

LEADER = 1
POSSIBLE_LEADER = 0

for commiter in large_commiter.keys():
    if commiter in large_author.keys():
        leaders[commiter]= LEADER
    else:
        leaders[commiter] = POSSIBLE_LEADER

passengers = dict()
PASSENGER = 1
POSSIBLE_PASSENGER = 0

for  commiter in small_commiter.keys():
    if commiter in small_author.keys():
      passengers[commiter] = PASSENGER
    else:
       passengers[commiter] = POSSIBLE_PASSENGER


if PASSENGER in passengers.values():
    print('Project has passenger')

if LEADER in leaders.values():
    print('Project is leading by someone')

if len(leaders) and len(passengers):
    print('Project is unevenly contributed')
elif len(leaders) or len(passengers):
    print('Project might be unevenly contributed')