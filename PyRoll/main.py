### PyPoll
#
#![Vote-Counting](Images/Vote_counting.jpg)
#
#* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#
#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#
#  * The total number of votes cast
#
#  * A complete list of candidates who received votes
#
#  * The percentage of votes each candidate won
#
#  * The total number of votes each candidate won
#
#  * The winner of the election based on popular vote.
#
#* As an example, your analysis should look similar to the one below:
#
#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```
#
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# Imports the OS and CSV modules necessary to complete the exercise
import os
import csv

# Establishes list variables that I will append later with a for loop
candidate = []
unique_candidates = []
unique_candidates_count = []
unique_candidates_perc = []
report = []
 
#Opens the directory that contains the csv file, sets the delimiter as ",", and establishes the variable csvfile as the data file
resource_csv = os.path.join('../PyRoll/Resources', 'election_data.csv')
with open(resource_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvfile = csv.reader(csvfile)
    csv_header = next(csvreader)

# For Loop that adds every instance of a candidate to the variable candidate. Then it only adds a new candidate to the list unique_candidates if there is not already an instance of that name in the list.    
    for row in csvfile:
        candidate.append(row[2])
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])

# Calculates the length of the list candidate and sets the variable total_votes to that number.             
    total_votes = len(candidate)
    
 # For Loop that  appends the list unique_candidate_count with the count of the people in the unique_candidates list. Also appends the unique_candidates_perc with the % calculation based on the unique_candidates list.
    for people in unique_candidates:
        unique_candidates_count.append(candidate.count(people))
        unique_candidates_perc.append(round(candidate.count(people)/total_votes*100,2))
   
 # establishes the winner by using the max function to find the highest number in the unique candidate count. Then it uses that index to choose the corresponding name in unique candidates and assigns that to the variable 'winner'
    winner = unique_candidates[unique_candidates_count.index(max(unique_candidates_count))]
    
   
# Appends my report list with the strings of text I want to print later as well as my total vote count
    report.append('Election Results''\n')
    report.append('-----------------------------------\n')
    report.append('Total Votes: '+str(total_votes)+'\n')
    report.append('-----------------------------------\n')

# For Loop that will add a new line of text for the candidate, their total vote %, and their total vote count and then appends my report list with those lines in order
    for i in range(len(unique_candidates)):
        report.append(str(unique_candidates[i])+':  '+str(unique_candidates_perc[i])+'%  ('+str(unique_candidates_count[i])+')\n')
   
# Appends my report list with the strings of text I want to print later as well as my twinner    
    report.append('-----------------------------------\n')
    report.append('Winner:   '+str(winner)+'\n')
    
    
 # Prints my report list to the console using a for loop to print each line individually    
    for line in report:
        print(line, end = '')
        
 # Creates a text file that contains the information in my report    
    with open('election_results.txt','w') as output:
        output.writelines(report)
