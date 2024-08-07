import os
import csv

# path to file
file_path = os.path.join("Resources", "election_data.csv")

# Variables
total_votes = 0
candidates_votes = {}
candidates = []

# Election data file
with open ("Resources/election_data.csv", 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  
    
    # Skip header row
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        
        if candidate not in candidates:
            candidates.append(candidate)
            candidates_votes[candidate] = 1
        else:
            candidates_votes[candidate] += 1

# Calculate the percentage of votes each candidate got
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates_votes.items()}

#Determine the winner
winner = max(candidates_votes, key=candidates_votes.get)

#print analysis results
print("Election Results:")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates_votes.items():
    print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({candidates_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Export results to text file
with open("election_results.txt", "w") as output_file:
    output_file.write("Election Results:\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidates_votes.items():
        output_file.write(f"{candidate}: {percentage_votes[candidate]:.3f}% ({candidates_votes[candidate]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
    