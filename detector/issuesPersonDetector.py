import sys

from extractor.extractor import features
from extractor.filter import filter

author_filter = features['issues_person']

large_author = author_filter.large()

print("large number of issues post by single user")
count= 0
for author, result  in large_author.iteritems():

    print('person%s,issues: %s, percentage: %s' %(count, result[0], result[1]))
    count+=1

small_author = author_filter.small()

print("small number of issues post by single user")
count=0
for author, result  in small_author.iteritems():
    print('person%s,issues: %s, percentage: %s' %(author, result[0], result[1]))
    count+=1