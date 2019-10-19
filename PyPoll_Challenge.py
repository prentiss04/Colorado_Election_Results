# Pyton code to analyze voting results from a subset of Colorado counties. 
# Code can be scaled, both in counties and candidates. 
# County segmentation could be accomplished with code manipulation (e.g. county breakdown by candidate, or candidate breakdown by county)
# If additional demographics are added to the underlying data, the code will need to be modified with Boolean logic. 

# Dependencies added.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path. (!!! not sure this step is working !!!)
file_to_save = os.path.join("Resources", "Election_Analysis", "analysis", "election_analysis.txt")
print(file_to_save)

# Using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:

# Candidate variables, lists and dictionaries

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []
# Declare the empty vote dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County variables, lists and dictionaries

# County tally 
# establish county vote counter
total_county_counter = 0
# County options list
county_options = []
# Declare the empty county tally dictionary
county_votes = {}
# Leading county and leading count tracker
leading_county = ""
leading_county_count = 0
leading_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
 
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the csv file.
    for row in file_reader:
        # Add to the total vote count and total county vote tally though this may be unneccessary since total votes will be the same whether they are for candidate or from county
        total_votes +=1
        total_county_counter +=1

        # Print the candidate name from each row and county
        candidate_name = row[2]
        county_name = row[1]

# Determination of candidate voting results

        # If the candidate does not match any existing candidate... 
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

# **************************************************************************************************************************

# Determination of county turnout results

        # If the county name does not match any existing county ...
        if county_name not in county_options: 
            # Add it to the list of counties
            county_options.append(county_name)

            # Begin tracking that county's tally
            county_votes[county_name] = 0

        # Add a "vote" to that county's tally
        county_votes[county_name] +=1

# **************************************************************************************************************************

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n")

    print(election_results, end="")

    # Save the final vote count to the text file. Consider adding initials to top of header as distinguising marker
    # txt_file.write("PPD")
    txt_file.write(election_results)

# **************************************************************************************************************************

# County Participation 

    # Determine the percentage of votes cast in each county by looping through the counts.
    print("\nCounty Votes:")
    txt_file.write("\nCounty Votes:\n")

    for county_name in county_votes:
        # Retrieve vote tally in each county
        tally = county_votes[county_name]
        # Calculate the percentage of votes.
        tally_percentage = float(tally) / float(total_county_counter) * 100
        
        # String for individual county results
        county_results = (f"{county_name}: {tally_percentage:0.1f}% ({tally:,})\n")

        # Print each county, their vote tally, and percentage to the terminal. 
        print(county_results)

        # Save the winning county's name to the text file.
        txt_file.write(county_results)
        
        # Determine if the votes are greater than the winning tally
        if (tally > leading_county_count) and (tally_percentage > leading_county_percentage):
            # If true then set leading_county_count = tally and leading percentage 
            leading_county_count = tally
            
            # tally percentage
            leading_percentage = tally_percentage
            
            # Set the leading county equal to the county's name
            leading_county = county_name

    leading_county_summary = (
        f"\n--------------------\n"
        f"Largest County Turnout: {leading_county}\n"
        f"---------------------\n")
    print(leading_county_summary)
    
    # Save the leading county's results to the text file.
    txt_file.write(leading_county_summary)

# **************************************************************************************************************************
      
    # Determine the percentage of votes for each candidate by looping through the counts.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Name the candidate results variable
        candidate_results = (f"{candidate}: {vote_percentage:0.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal. 
        print(candidate_results)

        # Save the winning candidate's name to the text file.
        txt_file.write(candidate_results)
        
        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning percentage = 
            winning_count = votes
            
            # vote percentage
            winning_percentage = vote_percentage
            
            # Set the winning candidate equal to the candidate's name
            winning_candidate = candidate

    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
