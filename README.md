#Bad Smells Detector


##  Collection

##  Anonymization


##  Tables


###Issue Info


<table>
<thead>
<tr class="header">
<th align="left">issue Id</th>
<th align="left">State</th>
<th align="left">User</th>
<th align="left">Duration Time</th>
<th align="left">Closed Time</th>
<th align="left">Created Time</th>
<th align="left">Comments Num</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<th align="left">1 # </th>
<th align="left">closed</th>
<th align="left">user0</th>
<th align="left">14143</th>
<th align="left">1428367982</th>
<th align="left">1428353839</th>
<th align="left">2</th>

</tr>
<tr class="even">
<th align="left">2 #</th>
<th align="left">closed</th>
<th align="left">user0</th>
<th align="left">452566</th>
<th align="left">1424060565</th>
<th align="left">1423607999</th>
<th align="left">0</th>
</tr>
</tbody>
</table>

[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/issuesData_1.csv)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/issuesData_2.csv)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/issuesData_3.csv)


###Commit Info

#### Commit By Person
<table>
<thead>
<tr>
<th>Commiter</th>
<th>Created Time</th>
</tr>
</thead>
<tbody>
<tr>
<td>user_0</td>
<td>1474778.0</td>
</tr>
<tr>
<td>user_1</td>
<td>1423456.0</td>
</tr>
</tbody>
</table>

[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/project1_commits.csv)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/project2_commits.csv)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/project3_commits.csv)


####Commit Per Week

<table>
<thead>
<tr>
<th>Start week</th>
<th>Commit Number</th>
</tr>
</thead>
<tbody>
<tr>
<td>2015-04-03 00:00:00</td>
<td>12</td>
</tr>
</tbody>
</table>

[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/project1_commits_week.csv)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/project2_commits_week.csv)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/project3_commits_week.csv)



###Pull Request Info

<table>
<thead>
<tr class="header">
<th align="left">Pull Request</th>
<th align="left">changed_files</th>
<th align="left">mergeable(T/F)</th>
<th align="left">process_duration(hours)</th>

</tr>     
</thead>
<tbody>
<tr class="odd">
<td align="left">Request # </td>
<td align="left">10</td>
<td align="left">True</td>
<td align="left">1</td>
   
</tr>
<tr class="even">
<td align="left">Request #</td>
<td align="left">40</td>
<td align="left">False</td>
<td align="left">10</td>  
</tr>
</tbody>
</table>

[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/Pull_1.txt)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/Pull_2.txt)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/Pull_3.txt)

###Milestone Info
<table>
<thead>
<tr class="header">
<th align="left">MileStone</th>
<th align="left">Late Milestone(T/F)</th>
<th align="left">Total Issues</th>
<th align="left">Closed Issues</th>
<th align="left">Open Issues</th>
<th align="left">Due on(datetime)</th>
<th align="left">Duration(days)</th>
</tr>     
</thead>
<tbody>
<tr class="odd">
<th align="left">MileStone # </th>
<th align="left">False</th>
<th align="left">20</th>
<th align="left">20</th>
<th align="left">0</th>
<th align="left">2015-04-14T19:59:29Z</th>
<th align="left">20</th>
   
</tr>
<tr class="even">
<th align="left">MileStone #</th>
<th align="left">True</th>
<th align="left">21</th>
<th align="left">19</th>
<th align="left">2</th>
<th align="left">2015-04-01T19:29:29Z</th>
<th align="left">inf</th> 
</tr>
</tbody>
</table>




[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/MileStone_1.txt)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/MileStone_2.txt)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/MileStone_3.txt)


##  Data


[project1] (https://github.com/CSC510/BadSmells/tree/master/data/group1)

[project2] (https://github.com/CSC510/BadSmells/tree/master/data/group2)

[project3] (https://github.com/CSC510/BadSmells/tree/master/data/group3)




### Data samples



##  Feature detection & Result
####1. Unusual duration of issues
The time each issue lasted can represent the efficiency of the team, and tell whether the issue was created reasonably or not. If the duration of one issue is unusually long, it might be a big problem which need to be divided into several sub-problems. If one issue last short, then the issue might be a small problem which need not open an issue.

#####Result
We have collected issue data from each group and we calculate the duration of each issue to get the duration in hours, as shown below. 

		duration in hours 
		
		group1: [12, 0, 241, 241, 1025, 1068, 1069, 1069, 241, 19, 1044, 4, 1026, 26, 0, 13, 1023, 25, 740, 724, 8, 1309, 20, 1, 21, 3, 15, 1, 0, 17, 4, 24, 0, 790, 1160, 280, 479, 912, 1310, 1309, 974, 260, 13, 304, 304, 13, 13, 479]
		group2: [26, 26, 28, 34, 1, 46, 49, 47, 29, 74, 103, 122, 109, 73, 73, 5, 65, 65, 32, 268, 232, 183, 288, 303, 220, 459, 474, 501, 838, 231, 126, 220, 281, 243, 340, 242, 76, 12, 357, 363, 364, 114, 19, 18, 144, 46, 67, 52, 121, 0, 554, 554, 554, 554, 554, 1, 22, 221, 0, 557, 575, 579, 646]
		group3: [0, 122, 279, 16, 268, 6, 1, 1, 277, 16, 16, 17, 17, 18, 18, 18, 18, 17, 17, 280, 3, 0, 18, 26, 48, 26, 29, 47, 11, 39, 49, 41, 41, 41, 41, 41, 3, 83, 12, 65, 358, 740, 934, 156, 158, 937, 169, 0, 182, 202, 0, 235, 61, 263, 54, 1058, 1110, 72, 0, 32, 192, 400, 372, 1, 91, 372, 0, 125]
		
####2. None issue time
If one issue last extremely short, nearly no time, then the issue might be created by mistake, or the bug was too small to report.

#####Result<a name="issue"></a>
According to the data we collected in feature 1, we will be able to get the duration of time,as shown [above](#issue). 


####3. Unusually long time spent in a specific milestone
When open a milestone, it means that the team is facing a difficult subject, or having a relatively high goal. If one milestone consumed too much time, then we might regard it as problematic, because the tasks might be too complex, or the goal might be too high to meet.

#####Result


####4. Time spent in a milestone is unusually short
When a milestone lasted extremely short, we can also say that it is not reasonable, because it might probably be reduced into one or two issues.

#####Result


####5. Large number of issues in a specific milestone
If there are large number of issues created in a milestone, it might be the case that the milestone is too complex to achieve. It may probably be more efficient to divide the complex milestone into two or more small and relatively easy milestones.

#####Result


####6. Small number of issues in a specific milestone
If the number of issues opened in a milestone is too small, it can be replaced by some issues. Because when milestone is created, it should be a relatively long-term goal, not some goals which can be met in a short time.

#####Result


####7. Large number of issues posted by a single user
If a large percentage of issues were opened by one person, it is possible that the person was assigned tasks which were not suitable for him or her. It is also possible that the person is too busy while others are quite idle, which means that the work is not evenly distributed.

#####Result


####8. Small number of issues posted by a single user
When the number of issues opened by one user is extremely low, we may say that he or she might be a passenger who did not contribute much to the project.

#####Result


####9. Number of users involved in an issue
We found that sometimes one issue have no comment and feedback on it. It means that there is only one person got involved in this issue. In this case, we can say that other people may not totally understand this issue, or it is a relatively small problem which is not necessary to open an issue to deal with.

#####Result


####10. Unusual commits number in a specific time
Usually we think that the number of commits should be distributed evenly during one project. If during a certain period, there are too many commits, or just one or two commits, it could indicate that the period of time is too busy, or the period of time was not used efficiently.

#####Result


####11. Commits by a single user
If a large amount of commits were created by a single user, it reflects that the person undertook too much work. Or if a person gave commits which is unusually less, the person might be a passenger who need to be assigned more work.

#####Result


####12. Small Number of Pull Request
Pull request and branches in Github help a team finish their tasks efficiently. If the number of pull request and branches is unusually small, it is likely that the working process was not clear enough, or there were some communication problems between different teammates. A small pull request number also means that maybe they are using a hard way to do the merge rather than using pull request to do the merge.

#####Result
We collected the pull requests number and compared to the issue (number-requests number) to see how many percentage the pull request counts for.

####13. Long Process Tme of Pull Request
The process time of a pull request usually means whether the owner of the repo has an active involvement of a repo. 

#####Result<a name="pull"></a>
We collected the process time for each pull request of a specific repo, as shown below.
		
		pull request
		group1:
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
		
		group2:
		pull request
		changed_files : 20,	mergeable : True,	process_duration : 0.14
		
		group3:
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
		

####14. Large number of Files changed in a single Pull Request
The file changed for each pull request is also a feature we should monitor. If many files are changed in a single pull request, it will probably lead to more conflicts and increase the complexity of merge, thus giving more burden the repo manager. It could also means that it should be divided into two pull requests which only takes care of a specific issue or bug fixed.

#####Result
We collected the number of *file_changed* for each pull request of a specific repo, as shown [above](#pull). 


####15. Large number of Pull Request which can not be Auto-merged
The auto-mergeable attribute of a pull request is a blessing for repo manager, which means (s)he don't have to fix the conflicts caused by different developer. A large number of requests which can not be auto-mergeable is a disaster for a repo manager.

#####Result
We collect the data for each pull request and count the number of the pull request which cannot be auto-merged, as shown [above](#pull). 

####16. Unusual Number of time each label is used
Different labels in a project reflect different small topics, or different stages during the process. If the times one label was used is unusually small or large, it indicates that a certain stage in the project is relatively easy or difficult to achieve, and it can be replaced by a more reasonable label.

#####Result
We collected the number of *label used* a specific repo, as shown below.

		Label used each for label:
		group1: [12, 3, 6, 1, 19, 6, 5, 6, 4, 1, 3, 2, 1, 6, 1, 2, 9, 4, 11, 1, 4, 2, 2]
		group2: [15, 5, 1, 2, 2, 21, 5, 5, 2, 2]
		group3: [23, 33, 3, 9, 1, 6, 10]
 

####17. Number of Late Milestone
Whether a milestone is late or not can determine the team's schedule ability and whether everything is on the right track. A on-time milestone usually means a efficient feature delivery.

#####Result
We collect the data for each Milestone and count the number of the milestone which are late. 



##  Bad smells detector & Result

###Issue per Person Smell Detector

####Result

###Issue Duration Smell Detector
We calculate the mean value and standard deviation of each group's data and we define that most of the data should be include in the range of [mean-std,mean+std]. The data which is not in the range will be noticed as **unusual duration of issue**.

~~We define that the extremely small duration is within 6 minutes which is 0.1 hour. For a project like ours, taking almost 9 weeks, an issue lasting for only 6 minutes can hardly be called an issue. If the the duration is less than that, we name it None issue time.~~

####Result


###Commit per Person Smell Detector

####Result


###Label Usage Smell Detector
~~In case there are some extreme values, we have removed the largest and smallest one. Then we calculate the mean value and standard deviation for the times one specific label is used. Then the number which are larger than the upper bound which is average plus standard deviation or smaller than the lower bound which is average minus standard deviation will be noticed as unusual number of *label used*.~~

As said in the feature dectection, we have get the unusual use of labels whether it is tiny used or massively used. We define that the number of time used should be at the two standard deviation range of the mean value. Therefore:
	
	if number < mean + 

####Result


###Milestone Smell Detector
~~Then we calcuate the late milestone percentage for each repo.~~

####Result


###Pull Request Smell Detector
We collected the process time for each pull request of a specific repo.~~In case there are some extreme values, we have removed the largest and smallest one. Then we calculate the mean value and standard deviation for each list of time we get for each group. Then the process time which are larger than the upper bound which is average plus standard deviation will be noticed as long process time.

In case there are some extreme values, we have removed the largest and smallest one. Then we calculate the mean value and standard deviation for each list we get for each group. Then the number which are larger than the upper bound which is average plus standard deviation will be noticed as unusual large number of *file_changed*.

~~Then we calcuate the non auto-mergeable percentage for each repo.~~

####Result


##  Early warning & Result
###Issue per Person Early Warning

####Result

###Commit per Person Early Warning

####Result

