#Add dependencies
import os 
import csv
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a total vote counter
total_votes = 0
#Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: read and anlyze the data here
    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader: 
       # Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row 
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add votes to candidate count
        candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as txt_file:
          #Print final vote count to terminal
    election_results = (
            f"\nElection Results\n"
            f"---------------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------------\n")
    print(election_results, end="")
            # Save the final vote count to the text file
    txt_file.write(election_results)


    #Determine the percentage of votes for each candidate by looping through the counts
        #Iterate through the candidate list
    for candidate_name in candidate_votes:
            #Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
            #Calculate the percentage of votes
        vote_percentage = (float(votes) / float(total_votes)) * 100
            #Print the candidate name and percentage of votes
            #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

            #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Save candidate results to ou text file
        print(candidate_results)
        txt_file.write(candidate_results)
            #Determine winning vote count and candidate
            # Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
        # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

            #  To do: print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
# Close the file.

