# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

# Import the datetime dependency.
# import datetime
# Use the now() attribute on the datetime class to get the present time. 
# now = datetime.datetime.now()
# Print the present time
# print("The time right now is,",now)

#add our dependencies.
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


# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []
# Declare the empty vote dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0




# Open the election results and read the file.
with open(file_to_load) as election_data:

    # to do: read and analyze the data  here. 
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the csv file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate... 
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n")

    print(election_results, end="")

    # Save the final vote count to the text file. 
    txt_file.write(election_results)

      
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Interate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Name the candidate results variable
        candidate_results = (f"{candidate}: {vote_percentage:0.1f}% ({votes:,})\n")

        # Print the candidate name and percentage of votes.
        # Print each candidate, their voter count, and percentage to the terminal. 
        print(candidate_results)

        # Save the winning candidate's name to the text file.
        txt_file.write(candidate_results)
        
        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning percentage = 
            # vote percentage
            winning_count = votes
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




# ***********************************************************************************
#print(f"{candidate}: {vote_percentage:0.1f}% ({votes:,})\n")




# Print the candidate vote dictionary.
#print(candidate_votes)

# Print the candidate list
#print(candidate_options)

# Print the total votes.
#print(total_votes)




#    print(election_data)

# Close the file
#election_data.close()



# Using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()

# Using the open() function with the "w" mode we will write data to the file. 
#open(file_to_save, "w")


