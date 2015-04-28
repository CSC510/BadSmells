import sys

from extractor.extractor import features
from extractor.filter import filter

weeks_filter = features['commits_week']

large_week = weeks_filter.large()

print("extra large work during the week")
count= 0
for week, result  in large_week.iteritems():

    print('week%s, commits: %s, percentage: %s' %(week, result[0], result[1]))
    count+=1

small_weeks = weeks_filter.small()

print("small work during the week")
count=0
for week, result  in small_weeks.iteritems():
    print('week%s, commits: %s, percentage: %s' %(week, result[0], result[1]))
    count+=1
