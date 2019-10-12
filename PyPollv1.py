import os

# Create a filename variable to a direct or indrect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
outfile.close()

# Using the open() function with the "w" mode we will write data to the file. 
open(file_to_save, "w")