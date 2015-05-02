# Bad Smells Detector


##  Collection
In the project, we got the data we needed by modifying gitable.py. With the help of APIs provided by Github, we extracted information from different projects. We collected data of issues, commits, milestones, and so on, with corresponding time information.

##  Anonymization
After we extracted the data, we anonymized them as required. All the names of users were replaced by user0, user1, and so on, and all the names of issues and milestones were replaced by numbers, or deleted directly. From the data, information on the original project can never be found.

##  Tables
After extracting data from github repositories using Github APIs, we applied anonymization process, and store the anonymized data into csv files or txt files. When analyzing data, we choose one or more parts in the data files, implemented with statistical methods like mean and standard deviation, and find characteristics of different projects. At last, we check the data and combine them to find if there is bad smell in projects.

## Data samples

####1. Milestone info
late | total issues | closed issues | due time | close time | duration time | open issues
---- | ---- | ---- | ---- | ---- | ---- | ----
True | 19 | 19 | 2015-03-10T04:00:00Z | 2015-03-22T19:57:55Z | 24.87 | 0
False | 14 | 14 | 2015-02-28T05:00:00Z | 2015-02-26T17:09:17Z | 7.79 | 0

[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/MileStone_1.txt)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/MileStone_2.txt)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/MileStone_3.txt)

####2. Pull request info
changed files | mergeable | duration time
---- | ---- | ----
1 | True | 0.91
21 | True | 2034

[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/Pull_1.txt)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/Pull_2.txt)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/Pull_3.txt)

####3. Issue number per week
week 1 | week 2 | week 3 | week 4 | week 5 | week 6 | week 7 | week 8 
---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
7 | 2 | 6 | 4 | 6 | 11 | 21 | 6
8 | 23 | 1 | 2 | 16 | 13 | 5 | 

[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/issuesByWeek_1.txt)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/issuesByWeek_2.txt)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/issuesByWeek_3.txt)

####4. Issue info
issue_id | state | user | duration time | closed time | create time | comments number
---- | ---- | ---- | ---- | ---- | ---- | ----
23 | closed | user1 | 2937 | 1424300731 | 1424297794 | 1
41 | closed | user0 | 1037100 | 1427248965 | 1426211865 | 12

[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/issuesData_1.csv)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/issuesData_2.csv)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/issuesData_3.csv)

####5. Commit info
user | commit time
---- | ----
person_0 | 1428613428.0
person_2 | 1423220949.0

[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/project1_commits.csv)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/project2_commits.csv)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/project3_commits.csv)

####6. Commit number per week
week 1 | week 2 | week 3 | week 4 | week 5 | week 6 | week 7 | week 8 | week 9 | week 10 | week 11
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
2 | 9 | 16 | 6 | 7 | 72 | 7 | 2 |  |  | 
4 | 13 | 45 | 56 | 56 | 56 | 27 | 56 | 59 | 133 | 4

[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/project1_cimmits_week.csv)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/project2_cimmits_week.csv)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/project3_cimmits_week.csv)


##  Feature detection
####1. Unusual period of issues
The time each issue lasted can represent the efficiency of the team, and tell whether the issue was created reasonably or not. If the period of one issue is unusually long, it might be a big problem which need to be divided into several sub-problems. If one issue last   short, then the issue might be a small problem which need not open an issue.

####2. None issue time
If one issue last extremely short, nearly no time, then the issue might be created by mistake, or the bug was too small to report.

####3. Unusually long time spent in a specific milestone
When open a milestone, it means that the team is facing a difficult subject, or having a relatively high goal. If one milestone consumed too much time, then we might regard it as problematic, because the tasks might be too complex, or the goal might be too high to meet.

####4. Time spent in a milestone is unusually short
When a milestone lasted extremely short, we can also say that it is not reasonable, because it might probably be reduced into one or two issues.

####5. Large number of issues in a specific milestone
If there are large number of issues created in a milestone, it might be the case that the milestone is too complex to achieve. It may probably be more efficient to divide the complex milestone into two or more small and relatively easy milestones.

####6. Small number of issues in a specific milestone
If the number of issues opened in a milestone is too small, it can be replaced by some issues. Because when milestone is created, it should be a relatively long-term goal, not some goals which can be met in a short time.

####7. Large number of issues posted by a single user
If a large percentage of issues were opened by one person, it is possible that the person was assigned tasks which were not suitable for him or her. It is also possible that the person is too busy while others are quite idle, which means that the work is not evenly distributed.

####8. Small number of issues posted by a single user
When the number of issues opened by one user is extremely low, we may say that he or she might be a passenger who did not contribute much to the project.

####9. Number of users involved in an issue
We found that sometimes one issue have no comment and feedback on it. It means that there is only one person got involved in this issue. In this case, we can say that other people may not totally understand this issue, or it is a relatively small problem which is not necessary to open an issue to deal with.

####10. Unusual commits number in a specific time
Usually we think that the number of commits should be distributed evenly during one project. If during a certain period, there are too many commits, or just one or two commits, it could indicate that the period of time is too busy, or the period of time was not used efficiently.

####11. Commits by a single user
If a large amount of commits were created by a single user, it reflects that the person undertook too much work. Or if a person gave commits which is unusually less, the person might be a passenger who need to be assigned more work.

####12. Number of pull request/branches
Pull request and branches in Github help a team finish their tasks efficiently. If the number of pull request and branches is unusually large or small, it is likely that the working process was not clear enough, or there were some communication problems between different teammates.

####13. Number of time each label is used
Different labels in a project reflect different small topics, or different stages during the process. If the times one label was used is unusually small or large, it indicates that a certain stage in the project is relatively easy or difficult to achieve, and it can be replaced by a more reasonable label.


##  Feature detection results

##  Bad smells detector

##  Bad smells results

##  Early warning

##  Early warning results
