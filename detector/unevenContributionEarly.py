
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from extractor.extractor import weekly_issues, weekly_commits , draw_bar
from extractor.filter import filter
from unevenContributionDetector import uneven

week_issues = []
weeks = weekly_issues.keys()
weeks.sort()
for week in weeks:
    week_issues.append(weekly_issues.get(week))

week_commits = []
for week in  weekly_commits.keys():
    if week not in weeks:
        weeks.append(week)
weeks.sort()
for week in weeks:
    week_commits.append(weekly_commits.get(week))

authors_commits = dict()
authors_issues = dict()
detection_result = []
for i in range(len(weeks)):
    week = weeks[i]
    commits = weekly_commits.get(week)
    if commits:
        for author, num in commits.iteritems():
            if not authors_commits.get(author):
                authors_commits[author] = 0
            authors_commits[author] = authors_commits[author]+ num

    issues= weekly_issues.get(week)
    if issues:
        for author , num in issues.iteritems() :
            if not authors_issues.get(author):
                authors_issues[author] = 0
            authors_issues[author] = authors_issues[author]+ num


    print("From week 0-%d" %(i))


    commits_filter = filter(authors_commits)
    issues_filter = filter(authors_issues)
    degree = uneven(commits_filter.large(), commits_filter.small(), issues_filter.large(), issues_filter.small())
    detection_result.append(degree)

data = detection_result
width =0.35
ind = np.arange(len(data))
fig, ax = plt.subplots()
rest = ax.bar(ind+width, data, width, color='r')
ax.set_title("Early uneven distribution detection")
ax.set_ylabel("Badsmell degree")
ax.set_xlabel("week")

ax.set_xticks(ind+width)
ax.set_xticklabels(range(len(detection_result)))
plt.show()