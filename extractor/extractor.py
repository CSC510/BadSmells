__author__ = 'jentle'


import sys
import filter
import logging
import gitable
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(name)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def  process_issues(features):
    issues = gitable.launchDump()
    weekly_issues = issues['week']
    del issues['week']

    author_issues = dict()
    events_issues =dict()
    comments_issues = dict()
    for issue, events in issues.iteritems():
        #print("ISSUE " + str(issue))


        dict_add(author_issues, events[0].user)

        dict_add(comments_issues, events[0].comments)

        dict_add(events_issues, len(events[1:]))


    draw_bar(author_issues.values(), "issues number posted by person","issues", range(len(author_issues.keys())),"person",0.35)
    print(comments_issues)
    author_filter = filter.filter(author_issues)
    large_author = author_filter.large()
    if(len(large_author) >0 ):
        features['large issues post by single user'] = large_author

    small_author = author_filter.small()
    if(len(small_author) >0 ):
        features['small issues post by single user'] = small_author

    draw_bar(comments_issues.values(),"issues number with same comments number","issues",comments_issues.keys(),"comments number",0.35)
    print(events_issues)
    events_filter= filter.filter(events_issues)
    if len(events_filter.large())>0:
        features['large issues with same events'] = events_filter.large()

    comments_filter = filter.filter(comments_issues)
    large_comments = comments_filter.large()
    if(len(large_comments)>0):
        features['large issues with same comments'] = large_comments
    draw_bar(events_issues.values(),"issues number with same events number", "issues",events_issues.keys(),"events number",0.35)
    single_user = filter.filter(author_issues)
    single_user.large(5)

def draw_bar(data, title, ylabel, xaix, xlabel, width=0.35):
    ind = np.arange(len(data))
    fig, ax = plt.subplots()
    rest = ax.bar(ind+width, data, width, color='r')
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_xticks(ind+width)
    ax.set_xticklabels(xaix)
    #plt.show()

def dict_add(dict, item):
    if not dict.get(item):
        dict[item]  = 0
    dict[item] += 1

def process_commits(features):
    commits_dict = gitable.dumpCommits()
    weeks = dict()
    all = dict()

    for author, commits in commits_dict.iteritems():
        all[author] = len(commits[1:])
        for week in commits[0].keys():
            if not weeks.get(week):
                weeks[week] = dict()
            week_count = weeks.get(week)

            num= commits[0].get(week)
            week_count[author]  = num
            weeks[week]  = week_count
    weekly = weeks.keys()
    weekly.sort()
    weekly_count = dict()
    sorted_week_count = []
    for week in weekly:

        commit_week = filter.filter(weeks.get(week))
        large = commit_week.large(0.25, percent=True)
        small = commit_week.small(0.1,percent = True)
        weekly_count[week]  = commit_week.sum()
        sorted_week_count.append(commit_week.sum())
        print('%s, %d' %(week, commit_week.sum()))
        #logger.info(large)
        #logger.info(small)

    # Uneven work of weeks
    draw_bar(sorted_week_count,"commits per week","commits",range(len( sorted_week_count)),"week",0.35)
    week_filter = filter.filter(weekly_count)
    small_weeks = week_filter.small()
    if len(small_weeks)>0:
        features['low commits during the gap time']= small_weeks
        logger.info(small_weeks)
    large_weeks  =week_filter.large()
    if len(large_weeks)>0:
        features['extra large work during the week'] = large_weeks
        #logger.info(large_weeks)
    #logger.info(large_weeks)


    # Uneven contribute of workers
    draw_bar(all.values(), "commits number posted by person","issues", range(len(all.keys())),"person",0.35)
    contribution_filter =filter.filter(all)
    leader  = contribution_filter.large(delta=1)
    if len(leader)>0 :
        features['large commits by single user']  =  leader

        #logger.info("Project has leader %s" %(leader))
    passenger  = contribution_filter.small(delta=1)
    if len(passenger)>0 :
        features['small commits by single user']= passenger
        #logger.info("Project has passenger %s" %(passenger))
    #logger.info(all)


def main():
    features = dict()
    process_issues(features)
    process_commits(features)
    for feature , result in features.iteritems():
        print('%s,%s' %(feature, result))




if __name__ ==  "__main__":
    main()