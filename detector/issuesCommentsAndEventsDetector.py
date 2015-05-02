import sys

from extractor.extractor import features
from extractor.filter import filter

comments_filter = features['comments_issues']

large_comments= comments_filter.large()

print('large issues with same comments')
count= 0
for comments, result  in large_comments.iteritems():

    print('comments: %d,issues: %s, percentage: %s' %(comments, result[0], result[1]))
    count+=1

events_filter = features['events_issues']

large_events= events_filter.large()

print("issues number with same events number")
count= 0
for event, result  in large_comments.iteritems():

    print('events: %s,issues: %s, percentage: %s' %(event, result[0], result[1]))
    count+=1
