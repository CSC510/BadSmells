 # Bad Smells Detector


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


####2. None issue time
If one issue last extremely short, nearly no time, then the issue might be created by mistake, or the bug was too small to report.

#####Result



####3. Unusal duration time of milestone

In this part, we amied to detect each milestone's duration time and find abnormal time schedule during the whole project. The code for collecting milestone duration time data can be found here (gittable).

Data results:
[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/MileStone_1.txt)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/MileStone_2.txt)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/MileStone_3.txt)

Project1:

Badsmell: This milestone has Xsmall time.
Milestone time is normal
Milestone time is normal
Milestone time is normal
Milestone time is normal

![Project1](https://github.com/CSC510/BadSmells/blob/master/imgs/project_1_MilestoneDuration.png)

Project2:

Badsmell: This milestone has Xsmall time.
Milestone time is normal
Milestone time is normal
Milestone time is normal
Badsmell: This milestone has Xsmall time.

![Project2](https://github.com/CSC510/BadSmells/blob/master/imgs/project_2_MilestoneDuration.png)

Project3:

Badsmell: This milestone has Xsmall time.
Milestone time is normal
Milestone time is normal

![Project2](https://github.com/CSC510/BadSmells/blob/master/imgs/project_3_MilestoneDuration.png)

Analysis:

Milestones are constructed to provide reference points along the road. This can be used to reassure developer that the proper path is being followed, and to indicate either distance travelled or the remaining distance to a destination. 

According to above three projects' milestone duration time, we can see that some milestone duration time are extremely large, others are small. If one milestone exists extremely valude, we might regard it as problematic, because the tasks might be too complex, or the goal might be too high to meet. 

We can calculate the mean value and standard deviation for each list of time we get for each group. Then the process time which are larger than the upper bound which is average plus standard deviation will be noticed as long process time. Then the process time which are smaller than the lower bound which is average minus standard deviation will be noticed as small process time. 


####4. Unusual number of issues in a specific milestone

For unususual number of issue in a specific milestone, it means that there exists some extremely large or small issues in a milestone. We can see this kind of milestone as abnormal milestone.

In this part, we have counted issues number for each milestone and found out the unusual number of issues in a specific milestone. 

Data results:
[project1] (https://github.com/CSC510/BadSmells/blob/master/data/group1/MileStone_1.txt)
[project2] (https://github.com/CSC510/BadSmells/blob/master/data/group2/MileStone_2.txt)
[project3] (https://github.com/CSC510/BadSmells/blob/master/data/group3/MileStone_3.txt)

Data Results:
Project1: 

![Project1](https://github.com/CSC510/BadSmells/blob/master/imgs/project_1_IssuePerMilestone.png)

Project2: 

![Project2](https://github.com/CSC510/BadSmells/blob/master/imgs/project_2_IssuePerMilestone.png)

Project3: 

![Project1](https://github.com/CSC510/BadSmells/blob/master/imgs/project_3_IssuePerMilestone.png)


Analysis:

According to above projects' data, we can see each different milestone has different issues number. Some of data are extremely small or big. We can use the method of analyzing mean and standard deviation of the data and find some abnormal data from the project.


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


####12. Number of pull request/branches
Pull request and branches in Github help a team finish their tasks efficiently. If the number of pull request and branches is unusually large or small, it is likely that the working process was not clear enough, or there were some communication problems between different teammates.

#####Result


####13. Number of time each label is used
Different labels in a project reflect different small topics, or different stages during the process. If the times one label was used is unusually small or large, it indicates that a certain stage in the project is relatively easy or difficult to achieve, and it can be replaced by a more reasonable label.

#####Result



##  Bad smells detector & Result

###Issue per Person Smell Detector

####Result

###Issue Duration Smell Detector

####Result

###Issue By Week Smell Detector

####Result


###Commit per Person Smell Detector

####Result


###Label Usage Smell Detector

####Result


###Milestone Smell Detector
According to milestone features memtioned above, we have collected milestone duration time and issues number in each milestone from three projects. We can see lots of projects' milestone duration time and issues number exist some extremely values. We have used the method of analyzing the mean and standard 
####Result


###Pull Request Smell Detector

####Result


##  Early warning & Result
###Issue per Person Early Warning

####Result

###Commit per Person Early Warning

####Result

