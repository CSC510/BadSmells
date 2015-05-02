# Bad Smells Detector #



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



##  Feature detection & Result
####1. Unusual duration of issues
The time each issue lasted can represent the efficiency of the team, and tell whether the issue was created reasonably or not. If the duration of one issue is unusually long, it might be a big problem which need to be divided into several sub-problems. If one issue last short, then the issue might be a small problem which need not open an issue.

#####Result
We have collected issue data from each group and we calculate the duration of each issue to get the duration in hours, as shown below. 

		duration in hours 
		
		Project1: [12, 0, 241, 241, 1025, 1068, 1069, 1069, 241, 19, 1044, 4, 1026, 26, 0, 13, 1023, 25, 740, 724, 8, 1309, 20, 1, 21, 3, 15, 1, 0, 17, 4, 24, 0, 790, 1160, 280, 479, 912, 1310, 1309, 974, 260, 13, 304, 304, 13, 13, 479]
		Project2: [26, 26, 28, 34, 1, 46, 49, 47, 29, 74, 103, 122, 109, 73, 73, 5, 65, 65, 32, 268, 232, 183, 288, 303, 220, 459, 474, 501, 838, 231, 126, 220, 281, 243, 340, 242, 76, 12, 357, 363, 364, 114, 19, 18, 144, 46, 67, 52, 121, 0, 554, 554, 554, 554, 554, 1, 22, 221, 0, 557, 575, 579, 646]
		Project3: [0, 122, 279, 16, 268, 6, 1, 1, 277, 16, 16, 17, 17, 18, 18, 18, 18, 17, 17, 280, 3, 0, 18, 26, 48, 26, 29, 47, 11, 39, 49, 41, 41, 41, 41, 41, 3, 83, 12, 65, 358, 740, 934, 156, 158, 937, 169, 0, 182, 202, 0, 235, 61, 263, 54, 1058, 1110, 72, 0, 32, 192, 400, 372, 1, 91, 372, 0, 125]
		
####2. None issue time
If one issue last extremely short, nearly no time, then the issue might be created by mistake, or the bug was too small to report.

#####<a name="issue">Result</a>
According to the data we collected in feature 1, we will be able to get the duration of time,as shown [above](#issue). 


####3. Unusal duration time of milestone

In this part, we aimed to detect each milestone's duration time and find abnormal time schedule during the whole project. Milestones are constructed to provide reference points along the road. This can be used to reassure developer that the proper path is being followed, and to indicate either distance travelled or the remaining distance to a destination. If one milestone lasts extremely long, we might regard it as problematic, because the tasks might be too complex, or the goal might be too high to meet.

#####Result

Project1:

![Project1](https://github.com/CSC510/BadSmells/blob/master/imgs/project_1_MilestoneDuration.png)

Project2:

![Project2](https://github.com/CSC510/BadSmells/blob/master/imgs/project_2_MilestoneDuration.png)

Project3:

![Project3](https://github.com/CSC510/BadSmells/blob/master/imgs/project_3_MilestoneDuration.png)


####4. Unusual number of issues in a specific milestone

For unususual number of issue in a specific milestone, it means that there exists some extremely large or small issues in a milestone. We can see this kind of milestone as abnormal milestone. In this part, we have counted issues number for each milestone and found out the unusual number of issues in a specific milestone. 

#####Result

Project1: 

![Project1](https://github.com/CSC510/BadSmells/blob/master/imgs/project_1_IssuePerMilestone.png)

Project2: 

![Project2](https://github.com/CSC510/BadSmells/blob/master/imgs/project_2_IssuePerMilestone.png)

Project3: 

![Project3](https://github.com/CSC510/BadSmells/blob/master/imgs/project_3_IssuePerMilestone.png)



####5. Large number of issues posted by a single user
If a large percentage of issues were opened by one person, it is possible that the person was assigned tasks which were not suitable for him or her. It is also possible that the person is too busy while others are quite idle, which means that the work is not evenly distributed.

#####Result
We sorted issues by user and generated the graph as follows:

*Project 1*
    ![](./imgs/project_1_issues_person.png)<br>
*Project 2*
    ![](./imgs/project_2_issues_person.png)<br>
*Project 3*
    ![](./imgs/project_3_issues_person.png)<br>
    
In order to extract the extra large number of issues post by a single user,we used the criteria in [issuesPersondector](/detector/issuesPersonDetector.py)
       
      issues_perosn >= mean + delta*standard_deviation    delta = 1

*project 1*
      large_issues post by single user : person2, issues: 27, percentage: 56.2%

*project 2*
      large_issues post by single user : person0, issues: 46, percentage: 73%

*project 3*
      large_issues post by single user : person0, issues: 45, percentage:66.1%



####6. Small number of issues posted by a single user
When the number of issues opened by one user is extremely low, we may say that he or she might be a passenger who did not contribute much to the project.

#####Result

Using the above data collected, we also detected extra small number of issues by single user[issuesPersondector](/detector/issuesPersonDetector.py)
       
      issues_person <= mean - delta*standard_deviation    delta = 1


*project 1*
      small_issues post by single user : None

*project 2*
      small_issues post by single user : None

*project 3*
      small_issues post by single user : None 
>>>>>>> develop


####7. Number of users involved in an issue
We found that sometimes one issue have no comment and feedback on it. It means that there is only one person got involved in this issue. In this case, we can say that other people may not totally understand this issue, or it is a relatively small problem which is not necessary to open an issue to deal with.

#####Result

We sorted the issues number according to the comments number. 
We also sorted the issues number according to the events number in this issue [issuesCommentsAndEventsDetector](/detector/issuesCommentsAndEventsDetector.py):

*Project 1*
    ![](./imgs/project_1_comments_issues.png)  
    ![](./imgs/project_1_events_issues.png) <br> 

    1.large issues number  with same comments:
        comments: 1, issues: 27 , percentage: 54.1%
    2.large issues number with same events:
        events: 2, issues: 11, percentage: 22.9%
        events: 3, issues: 9 , percentage: 18.75
*Project 2*
    ![](./imgs/project_2_comments_issues.png)  
     ![](./imgs/project_2_events_issues.png) <br> 
    
    1.large issues number  with same comments:
        comments: 1, issues: 29 , percentage: 46.0%
    2.large issues number with same events:
        events: 1, issues: 25, percentage: 39.6%
        events: 2, issues: 27 , percentage: 42.8%

*Project 3*
    ![](./imgs/project_3_comments_issues.png)  
    ![](./imgs/project_3_events_issues.png) <br> 
    
    1.large issues number  with same comments:
        comments: 0, issues: 41 , percentage: 60.3%
    2.large issues number with same events:
        events: 1, issues: 41, percentage: 60.3%

####8. Unusual commits number in a specific time
Usually we think that the number of commits should be distributed evenly during one project. If during a certain period, there are too many commits, or just one or two commits, it could indicate that the period of time is too busy, or the period of time was not used efficiently.

#####Result

We group the commits number in a week order and generated the graph as follows :[commitsPersondector](/detector/commitsPersonDetector.py)

*Project 1*
    ![](./imgs/project_1_commits_per_week.png)  

    1.extra large work during the week: week_5, commits:72
    2.small work during the week:NOne

*Project 2*
    ![](./imgs/project_2_commits_per_week.png)  

    1.extra large work during the week: 
        week_9, commits: 133, percentage: 26.1%
    2.small work during the week:NOne
        week_0, commits: 4, percentage: 0.7%
        week_10, commits: 4, percentage: 0.7%

*Project 3*
    ![](./imgs/project_3_commits_per_week.png)  

    1.extra large work during the week:
        week_2, commits: 42, percentage: 23.1%
        week_9, commits: 62, percentage: 34.1%
    2.small work during the week : None


####9. Commits by a single user
If a large amount of commits were created by a single user, it reflects that the person undertook too much work. Or if a person gave commits which is unusually less, the person might be a passenger who need to be assigned more work.

#####Result

We analyze the commits number commited by a single user and generate the graph as follows:[commitsWeekdector](/detector/commitsWeekDetector.py)

*Project 1*
    ![](./imgs/project_1_commits_person.png)  

    1.large commits by single user: None
    2.small commits by single user: None
    
*Project 2*
    ![](./imgs/project_2_commits_person.png)  
    
    1.large commits by single user: None
    2.small commits by single user: person2, commits:92, percentage: 18.0%

*Project 3*
    ![](./imgs/project_3_commits_person.png)  
    
    1.large commits by single user: person0, commits: 68, percentage: 37.3%
    2.small commits by single user: person3, commits: 22, percentage: 12.1%
    

####10. Small Number of Pull Request
Pull request and branches in Github help a team finish their tasks efficiently. If the number of pull request and branches is unusually small, it is likely that the working process was not clear enough, or there were some communication problems between different teammates. A small pull request number also means that maybe they are using a hard way to do the merge rather than using pull request to do the merge.


#####Result
We collected the pull requests number and compared to the issue (number-requests number) to see how many percentage the pull request counts for.

####11. Long Process Tme of Pull Request
The process time of a pull request usually means whether the owner of the repo has an active involvement of a repo. 

#####<a name="pull">Result</a>
We collected the process time for each pull request of a specific repo, as shown below.
		
		pull request
		Project1:
		changed_files : 1,	mergeable : True,	process_duration : 0.91
		changed_files : 1,	mergeable : True,	process_duration : 0.0
		changed_files : 2,	mergeable : True,	process_duration : 0.02
		changed_files : 1,	mergeable : True,	process_duration : 0.04
		changed_files : 21,	mergeable : True,	process_duration : 2.34
		changed_files : 12,	mergeable : True,	process_duration : 38.81
		changed_files : 1,	mergeable : True,	process_duration : 4.39
		changed_files : 10,	mergeable : True,	process_duration : 0.8
		changed_files : 15,	mergeable : True,	process_duration : 3.99
		changed_files : 1,	mergeable : True,	process_duration : 0.62
		changed_files : 5,	mergeable : True,	process_duration : 13.69
		changed_files : 1,	mergeable : True,	process_duration : 8.96
		changed_files : 15,	mergeable : True,	process_duration : 1.31
		changed_files : 5,	mergeable : True,	process_duration : 15.88
		changed_files : 1,	mergeable : True,	process_duration : 3.08
		changed_files : 4,	mergeable : True,	process_duration : 21.5
		changed_files : 3,	mergeable : True,	process_duration : 0.02
		changed_files : 11,	mergeable : True,	process_duration : 0.02
		changed_files : 3,	mergeable : True,	process_duration : 17.28
		changed_files : 4,	mergeable : True,	process_duration : 12.71
		changed_files : 2,	mergeable : True,	process_duration : 0.0
		changed_files : 1,	mergeable : True,	process_duration : 5.35
		
		Project2:
		pull request
		changed_files : 20,	mergeable : True,	process_duration : 0.14
		
		Project3:
		pull request
		changed_files : 8,	mergeable : True,	process_duration : 1.62
		changed_files : 16,	mergeable : True,	process_duration : 13.65
		changed_files : 1,	mergeable : True,	process_duration : 17.2
		changed_files : 6,	mergeable : True,	process_duration : 0.01
		changed_files : 9,	mergeable : True,	process_duration : 18.05
		changed_files : 4,	mergeable : True,	process_duration : 0.0
		changed_files : 3,	mergeable : True,	process_duration : 0.0
		changed_files : 19,	mergeable : True,	process_duration : 0.89
		changed_files : 30,	mergeable : True,	process_duration : 0.07
		changed_files : 44,	mergeable : True,	process_duration : 0.1
		changed_files : 3117,	mergeable : False,	process_duration : 0.95
		changed_files : 94,	mergeable : False,	process_duration : 64.82
		changed_files : 1,	mergeable : True,	process_duration : 0.01
		

####12. Large number of Files changed in a single Pull Request
The file changed for each pull request is also a feature we should monitor. If many files are changed in a single pull request, it will probably lead to more conflicts and increase the complexity of merge, thus giving more burden the repo manager. It could also means that it should be divided into two pull requests which only takes care of a specific issue or bug fixed.

#####Result
We collected the number of *file_changed* for each pull request of a specific repo, as shown [above](#pull). 


####13. Large number of Pull Request which can not be Auto-merged
The auto-mergeable attribute of a pull request is a blessing for repo manager, which means (s)he don't have to fix the conflicts caused by different developer. A large number of requests which can not be auto-mergeable is a disaster for a repo manager.

#####Result
We collect the data for each pull request and count the number of the pull request which cannot be auto-merged, as shown [above](#pull). 

####14. Unusual Number of time each label is used
Different labels in a project reflect different small topics, or different stages during the process. If the times one label was used is unusually small or large, it indicates that a certain stage in the project is relatively easy or difficult to achieve, and it can be replaced by a more reasonable label.

#####Result
We collected the number of *label used* a specific repo, as shown below.

		Label used each for label:
		Project1: [12, 3, 6, 1, 19, 6, 5, 6, 4, 1, 3, 2, 1, 6, 1, 2, 9, 4, 11, 1, 4, 2, 2]
		Project2: [15, 5, 1, 2, 2, 21, 5, 5, 2, 2]
		Project3: [23, 33, 3, 9, 1, 6, 10]
 

####15. Number of Late Milestone
Whether a milestone is late or not can determine the team's schedule ability and whether everything is on the right track. A on-time milestone usually means a efficient feature delivery.

#####Result
We collect the data for each Milestone and count the number of the milestone which are late. 



##  Bad smells detector & Result

###Uneven Contribution Smell Detector
In a project, someone may leading the project and someone could be a passenger with much less contribution to the group.
It may reflect on the issues and commits numbers by user. We conbine the commits and issues detector [unevenContributionDetector](./detector/unevenContributionDetector.py)
         
         leader: made both extra large issues and commits
         passenger: made both extra small large issues and commits 
         project is uneven contributed:  has both uneven issues and commits 
       

####Result
*Project1*
    Badsmells: None
    
*Project2*
    Badsmells:
       Project might be unevenly contributed
    
*Project3*
    Badsmells:
       Project is leading by someone
       Project is unevenly contributed


###Issue Duration Smell Detector
Method 1: To define the unusual length of the issue duration, we calculate the mean value and standard deviation of each group's data and we define that most of the data should be include in the range of [mean-std,mean+std]. The data which is not in the range will be noticed as **unusual duration of issue**.
We have also defined that the extremely small duration is within 6 minutes which is 0.1 hour. For a project like ours, taking almost 9 weeks, an issue lasting for only 6 minutes can hardly be called an issue. If the the duration is less than that, we name it None issue time.

		mean - std <= normal duration time of an issue <= mean + std
		amount of none issue < 5% of the total issue number
		
Method 2: We have sort the duration and pick the data at 10% (10% of the data is smaller this point, name it as A) and 90% (10% of the data is larger this point, name it as B). We have also picked out the medium value(name it as C) and then we calculate the slope of (A,C),k1 and (B,C),k2. If it varies a lot, for example, k2 is 8 times larger than k1. We denote it as badsmell as in this case the time spent on some issues increase expontienally compares to the small one, or it has only got very small numbers of issues which have medium length. Either way, it should be reported as a badsmell.

		k2<8* k1 =>normal issue duration
		
Detector code can be found [here](https://github.com/CSC510/BadSmells/blob/master/detector/issueDurationDetector.py) 

####Result

project 1:
		
	[12, 0, 241, 241, 1025, 1068, 1069, 1069, 241, 19, 1044, 4, 1026, 26, 0, 13, 1023, 25, 740, 724, 8, 1309, 20, 1, 21, 3, 15, 1, 0, 17, 4, 24, 0, 790, 1160, 280, 479, 912, 1310, 1309, 974, 260, 13, 304, 304, 13, 13, 479]
	Method 1
	('low val', 1, 'median val', 241, 'high val', 1069)
	('low pos', 4, 'median pos', 24, 'high pos', 43)
	BadSmell found in issue Duration
	Method 2
	('avg', 398.32608695652175, 'std', 456.46844047048609)
	('strange small count=', 0, 'strange large count=', 12, 'none issue count', 4)
	BadSmell found in issue Duration
		
project 2:

	[26, 26, 28, 34, 1, 46, 49, 47, 29, 74, 103, 122, 109, 73, 73, 5, 65, 65, 32, 268, 232, 183, 288, 303, 220, 459, 474, 501, 838, 231, 126, 220, 281, 243, 340, 242, 76, 12, 357, 363, 364, 114, 19, 18, 144, 46, 67, 52, 121, 0, 554, 554, 554, 554, 554, 1, 22, 221, 0, 557, 575, 579, 646]
	Method 1
	('low val', 18, 'median val', 122, 'high val', 554)
	('low pos', 6, 'median pos', 31, 'high pos', 56)
	Issue Duration Detector Passed
	Method 2
	('avg', 208.88524590163934, 'std', 196.02810925574465)
	('strange small count=', 5, 'strange large count=', 12, 'none issue count', 2)
	BadSmell found in issue Duration
		
project 3:

	[0, 122, 279, 16, 268, 6, 1, 1, 277, 16, 16, 17, 17, 18, 18, 18, 18, 17, 17, 280, 3, 0, 18, 26, 48, 26, 29, 47, 11, 39, 49, 41, 41, 41, 41, 41, 3, 83, 12, 65, 358, 740, 934, 156, 158, 937, 169, 0, 182, 202, 0, 235, 61, 263, 54, 1058, 1110, 72, 0, 32, 192, 400, 372, 1, 91, 372, 0, 125]
	Method 1
	('low val', 1, 'median val', 41, 'high val', 372)
	('low pos', 6, 'median pos', 34, 'high pos', 61)
	BadSmell found in issue Duration
	Method 2
	('avg', 140.15151515151516, 'std', 226.61235372622713)
	('strange small count=', 0, 'strange large count=', 7, 'none issue count', 6)
	BadSmell found in issue Duration

###Issue By Week Smell Detector
We have counted the number of issues per week, and analyzed the mean and standard deviation of issue numbers for each group. We consider the detectign result as a bad smell if the number of issue is less than mean minus standard deviation or the number of issue is greater than mean plus standard deviation. The issue duration smell detector will automatically report the detecting result when it analyze the project. Issue By Week Smell Detector can be found [issuesByWeekDetector](./detector/issuesByWeekDetector.py)

	issue number > mean + standard deviation or issue number < mean - standard deviation 
	or issueNum1 + issueNum2 < mean

####Result
The numbers of issues per week have been post in the feature and result part. Our smell detector reports the detecting results based on these sample data.

Project1: 

        [3, 19, 4, 5, 1, 1, 1, 14]
        Issues numbers are normal
        Badsmells: This week has too many issues.
        Issues numbers are normal
        Issues numbers are normal
        Issues numbers are normal
        Badsmells: This week has too less issues.
        Badsmells: This week has too less issues.
        Badsmells: This week has too many issues.

Project2: 

        [19, 9, 6, 4, 6, 1, 5, 13]
        Badsmells: This week has too many issues.
        Issues numbers are normal
        Issues numbers are normal
        Issues numbers are normal
        Issues numbers are normal
        Badsmells: This week has too less issues.
        Issues numbers are normal
        Issues numbers are normal

Project3:

        [10, 9, 7, 1, 1, 1, 1, 18, 20]
        Issues numbers are normal
        Issues numbers are normal
        Issues numbers are normal
        Issues numbers are normal
        Badsmells: This week has too less issues.
        Badsmells: This week has too less issues.
        Badsmells: This week has too less issues.
        Badsmells: This week has too many issues.
        Badsmells: This week has too many issues.


###Label Usage Smell Detector
To find out the bad smell in the label usage, we have removed the largest one, in case there are some extreme values. As we have observed in the pattern that there exists a label which stands for **finish**. A large majority of issues will be labelled as this when it comes to the final stage. Then we calculate the mean value and standard deviation for the times one specific label is used. We define the unusual use is the labels whether it is tiny used or massively used. We define that the number of time used should be at the two standard deviation range of the mean value. Detector source code can be checked [here](https://github.com/CSC510/BadSmells/blob/master/detector/labelUseDetector.py):
	
	 mean - std <= normal label used time <= mean + std 
	 
If labels which are denoted to have unusual usage exceeds 10% of the total number of labels, it will lead to badsmell.

####Result
	
project 1: 
	
	('avg', 4.1818181818181817)
	('std', 3.142615639535201)
	('number of strange low data', 5)
	('number of strange high data', 3)
	BadSmell found in Label Use
	
project 2:
	
	('avg', 4.333333333333333)
	('std', 4.0551750201988126)
	('number of strange low data', 0)
	('number of strange high data', 1)
	Label Use Detector Passed
	
project 3: 
	
	('avg', 8.6666666666666661)
	('std', 7.1336448530108996)
	('number of strange low data', 1)
	('number of strange high data', 1)
	BadSmell found in Label Use


###Milestone Smell Detector

According to milestone features memtioned above, we have collected milestone's duration time and issue number in each projects, and then analyzed the mean and standard deviation of duration time and issue numbers in each milestone. If duration time is short and issues number is large, we consider it as a bad smell. If duration time is long and issue number is small, we consider it as a bad smell too. [Milestone Smell Detector](./detector/milestoneDetector.py)

        duration time > mean + standard deviation and issues number < mean - standard deviation
        or
        duration time < mean - standard deviation and issues number > mean + standard deviation

Results

Project1: 
	
	Issue number in each milestone:  [1, 13, 6, 13, 6]
	Duration time in each milestone: [65.42, 1069.72, 1310.95, 304.98, 1310.28]
	Milestone duration time and issues number are normal
	Milestone duration time and issues number are normal
	Milestone duration time and issues number are normal
	Milestone duration time and issues number are normal
	Milestone duration time and issues number are normal

Project2:

	Issue number in each milestone:  [14, 19, 8, 7, 8]
	Duration time in each milestone: [186.93, 596.81, 652.64, 620.10, 264.00]
	Milestone duration time and issues number are normal
	Milestone duration time and issues number are normal
	Milestone duration time and issues number are normal
	Milestone duration time and issues number are normal
	Milestone duration time and issues number are normal

Project3:

	Issue number in each milestone:  [23, 4, 14, 23, 0]
	Duration time in each milestone: [876.85, 987.67, 987.43]
	**Badsmell: Milestone has too many issues in short time!**
	Milestone duration time and issues number are normal
	Milestone duration time and issues number are normal


###Pull Request Smell Detector
We have collected the details for each pull request of a specific repo such as **number of pull request,process time, file_changed, automergable**. We denote that for a normal project, its pull request should reach at least 10% of the commit number. And the process time shouldn't be too long, in case there are some extreme values, we have removed the largest and smallest one. Then we calculate the mean value and standard deviation for each list of time we get for each group. Same methods are used in define the unusual large number of file-changed in a single pull request. Whether automergeable pull request number is also a factor in define if there exists bad smell in a repo.

		normal number for pull request >= 5& of its commits number (a very very low requirements!! Should be higher!)
		mean - std <= normal process time of a pull request <= Min(mean + std, 72 hrs)
		mean - std <= normal file changed in a pull request <= mean + std

Detector Source Code can be found [here](https://github.com/CSC510/BadSmells/blob/master/detector/pullRequestDetector.py).
####Result

Project 1: 

	('Process Time', [0.91, 0.0, 0.02, 0.04, 2.34, 38.81, 4.39, 0.8, 3.99, 0.62, 13.69, 8.96, 1.31, 15.88, 3.08, 21.5, 0.02, 0.02, 17.28, 12.71, 0.0, 5.35])
	('Changed Files', [1, 1, 2, 1, 21, 12, 1, 10, 15, 1, 5, 1, 15, 5, 1, 4, 3, 11, 3, 4, 2, 1])
	('Pull request Number', 22, 'Commits number', 121)

	Process Time
	('avg', 5.6455000000000002, 'std', 6.6602526040684076)
	('number of strange small time', 0, 'number of strange large time', 5)

	 File Changed
	('avg', 4.9000000000000004, 'std', 4.7423622805517507)
	('number of strange large file changed', 5)
	Pull Request Detector Passed
	
Project 2:
	
	('Process Time', [0.14])
	('Changed Files', [20])
	('Pull request Number', 1, 'Commits number', 510)
	Too few pull request! BadSmell Detected

Project 3:
	
	('Process Time', [1.62, 13.65, 17.2, 0.01, 18.05, 0.0, 0.0, 0.89, 0.07, 0.1, 0.95, 64.82, 0.01])
	('Changed Files', [8, 16, 1, 6, 9, 4, 3, 19, 30, 44, 3117, 94, 1])
	('Pull request Number', 13, 'Commits number', 182)

	Process Time
	('avg', 4.7772727272727273, 'std', 7.1430412302134254)
	('number of strange small time', 0, 'number of strange large time', 3)

	 File Changed
	('avg', 21.272727272727273, 'std', 26.143279717360734)
	('number of strange large file changed', 1)
	Pull Request Detector Passed
	

##  Early warning & Result
### Issue number per week Early Warning

[earlyIssuesDetectorByWeek](./detector/earlyIssuesDetectorByWeek.py)

Result:
Project1: 

	[8, 2, 4, 1]
	Badsmells: This week has too many issues.
	Issues numbers are normal
	Issues numbers are normal
	Badsmells: This week has too less issues.

Project2:

	[19, 9, 6, 4]
	Badsmells: This week has too many issues.
	Issues numbers are normal
	Issues numbers are normal
	Issues numbers are normal

Project3:

	[10, 9, 7, 1]
	Issues numbers are normal
	Issues numbers are normal
	Issues numbers are normal
	Badsmells: This week has too less issues.

###Issue per Person Early Warning

####Result

###Commit per Person Early Warning

####Result

