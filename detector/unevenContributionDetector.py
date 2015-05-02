import sys
from issuesPersonDetector import large_author, small_author
from commitsPersonDetector import large_commiter,small_commiter

#compare if somebody made both most/smallest commits and issues

def uneven(large_commiter, small_commiter, large_author, small_author):
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

    result  = 0
    has_passenger = False
    possible_passenger = False
    if PASSENGER in passengers.values():
        has_passenger = True
        result += 2
        print('Project has passenger')
    elif POSSIBLE_PASSENGER in passengers.values():
        possible_passenger = True
        result +=  1
        print('Project might have passenger')

    has_leader = False
    possible_leader = False
    if LEADER in leaders.values():
        has_leader = True
        result += 2
        print('Project is leading by someone')
    elif POSSIBLE_LEADER in leaders.values():
        possible_leader = True
        result += 1
        print('Project might be leading by someone')

    if has_passenger or has_leader:
        print('Project is unevenly contributed')
    elif  possible_passenger or possible_leader:
        print('Project might be unevenly contributed')
    else:
        print('Project is evenly contributed')
    print("Uneven degree : %s" %(result))
    return result

uneven(large_commiter,small_commiter, large_author, small_author)