import sys

from extractor.extractor import features
from extractor.filter import filter

author_filter = features['commits_person']

large_commiter = author_filter.large()
small_commiter = author_filter.small()

print("large number of commits post by single user")

for author, result  in large_commiter.iteritems():

    print('person%s,commits: %s, percentage: %s' %(author, result[0], result[1]))




print("small number of commits by single user")
for author, result  in small_commiter.iteritems():
    print('person%s,commits: %s, percentage: %s' %(author, result[0], result[1]))
