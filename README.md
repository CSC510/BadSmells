# Bad Smells Detector


##  Collection

##  Anonymization

##  Tables

###Issue Info

###Commit Info

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
