import sys

from extractor.extractor import features
from extractor.filter import filter

author_filter = features['commits_person']

large_author = author_filter.large()

print("large number of commits post by single user")

for author, result  in large_author.iteritems():

    print('person%s,commits: %s, percentage: %s' %(author, result[0], result[1]))


small_author = author_filter.small()

print("small number of commits by single user")
for author, result  in small_author.iteritems():
    print('person%s,commits: %s, percentage: %s' %(author, result[0], result[1]))
