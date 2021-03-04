import os 
import csv

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and anlyze the data here
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)

#Print each row in the CSV file.
    

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:

#Write some data to the file.
    txt_file.write("Counties in the Election\n-----------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")

#Close the file
txt_file.close()

#The data we need to retrieve
#1. The total numbers of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5 The winner of the election based on popular vote

# Close the file.

