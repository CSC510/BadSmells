__author__ = 'jentle'


import sys
import filter
import logging
import gitable

if __name__ == "__main__":
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(name)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def  process_issues():
    issues = gitable.launchDump()
    weekly_issues = issues['week']
    del issues['week']

    author_issues = dict()
    for issue, events in issues.iteritems():
        print("ISSUE " + str(issue))

        user  = events[0].user
        if not author_issues.get(user):
            author_issues[user] = 0
        author_issues[user]  += 1
        #printm(events)

    single_user = filter.filter(author_issues)
    single_user.large(5)

def process_commits():
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
    for week in weekly:
        commit_week = filter.filter(weeks.get(week))
        result = commit_week.large(0.25, percent=True)
        logger.info(result)


    logger.info(all)

def main():

    process_issues()
    #process_commits()




if __name__ ==  "__main__":
    main()