# Analysis of the Election Audit

## Overview of the Election Audit
A Colorado Board of Elections employee has asked me to complete the election audit of a recent local congressional election by following the below tasks.

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Determine the number of votes cast in each county.
7. Determine the county with the highest turnout. 

#### Resources Used
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.52.1

## Election-Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- Votes by County:
    - There were 38,855 votes cast in Jefferson County, which accounted for 10.5% of the total number of votes in this precinct.
    - There were 306,055 votes cast in Denver County, which accounted for 82.8% of the total number of votes in this precinct.
    - There were 24,801 votes cast in Arapahoe County, which accounted for 6.7% of the total number of votes in this precint. 
- Denver County had the largest number of votes in this precinct. 
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 total votes.
    - Diana DeGette received 73.8% of the vote and 272,892 total votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 total votes.

## Election-Audit Summary
While this specific script was only used for this congressional district in Colorado, it can be applied to adapt for many other similar scenarios. As long as the we have data that includes counties in the 2nd column and the candidate that was voted for in the 3rd column, then this script should seamlessly output results for any district. We can also modify this script to include different types of data for this election or other elections. For example, if we wanted to know which candidate received the most votes from men or women, we could add a column from the voter data that includes the gender from each ballot ID. If we wanted to expand this data for a Colorado statewide election, that could also be done fairly easily. If you took a Colorado gubernatorial race and used data from all Colorado voters, this data would still output the total votes, votes by county, and the results/winner of the election. For this code to work, the counties and candiddates would still need to remain in their respective columns. The only difference is that there would be more total votes and many more counties listed. 
