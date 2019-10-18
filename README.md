# Colorado_Election_Results

## Project Overview
A Colorado Board of Elections manager has requested a efficient and streamlined process to analyze voting results in a recent election. If satisfied with the product, rollout to the entire state is a possibility. The following deliverables are expected. 

1. Determine the total number of votes cast. 
2. Provide a complete list of candidates who received votes. 
3. Determine the number of votes cast per candidate. 
4. Calculate the percentage of votes cast per candidate. 
5. Determine the winner of the popular vote. 

## Resources
- Date Source: election_results.csv
- Software: Python 3.6.1, Visual Studion Code 1.39.2, Anaconda 2019.10

## Summary:
The analysis of the election show the following: 
- There were 369,711 votes cast in the election
- The candidate results were: 
  - Charles Casper Stockam received 85,213 votes, comprising 23.0% of the total cast
  - Diana DeGette received 272,892 votes, comprising 73.8% of the total cast
  - Raymon Anthony Doane received 11,606 votes, comprising 3.1% of the total cast
- The winner of the popular vote was: 
  - Diana DeGette who received 272,892 votes, comprising 73.8% of the total cast

## Challenge Overview

In addition to the candidate results of the recent election the Board of Elections manager has requested additional information on the voter turnout in the respective counties. The output required is as follows:  

1. Determine the total number of votes cast. 
*2. Determine the number of votes cast in each county. (CHALLENGE DELIVERABLE)* 
_3. Document which county cast the greatest number of votes. (CHALLENGE DELIVERABLE)_
4. Provide a complete list of candidates who received votes. 
5. Determine the number of votes cast per candidate. 
6. Calculate the percentage of votes cast per candidate. 
7. Determine the winner of the popular vote. 

## Challenge Summary

The analysis of the election show the following: 
- There were 369,711 votes cast in the election
- Three counties provided 100% of the votes cast by the breakdown below
  - Jefferson County provided 38,855 votes, comprising 10.5% of the total cast
  - Denver County provided 306,055 votes, comprising 82.8% of the total cast
  - Araphahoe County provided 24,801 votes, comprising 6.7% of the total cast
- The largest turnout was:  
  - Denver County which cast 306,088 votes, comprising 82.8% of the total
- The candidate results were: 
  - Charles Casper Stockam received 85,213 votes, comprising 23.0% of the total cast
  - Diana DeGette received 272,892 votes, comprising 73.8% of the total cast
  - Raymon Anthony Doane received 11,606 votes, comprising 3.1% of the total cast
- The winner of the popular vote was: 
  - Diana DeGette who received 272,892 votes, comprising 73.8% of the total cast
  
## Further considerations
The data file that election officials provided contains a small sliver of voter information (county and candidate). While not requested 
by officials, we could have provided greater segmentation/breakdown. I.e. how did candidates fare in different counties or where did the 
greatest volume of votes for specific candidates come from. In our case with one large county providing the lions' share of the votes, 
the answers to some of the questions are fairly obvious. However as this project scales, answers to questions like these would be 
valuable. 

Furthermore, in addition to greater granularity, more voter information could inform future decisions. We were not provided with target 
populations for the respective counties. It could be interesting to see what counties, neighborhoods are participating in elections to 
inform officials of trends in voter enthusiasm or apathy. 
