# Python-Challenge
Homework Assignment #3

# PyBank and PyPoll Analysis

This repository has two Python scripts for the purpose of performing data analysis on financial records and election results. 

The PyBank script does a analysis on the CSV file containing financial data and finds the key metrics: total number of months, net profit/loss, and their changes over time. The Python script produces both terminal results and a text file of the results.

The PyPoll script does a analysis on a CSV file with election information, finding key information: total vote count, votes per candidate percentage, and the winner based on the most votes. It, too, outputs the results on terminal and a text file of the final results.

# Files

  PyBank: 
  -'main.py': The file with the Python script for the financial analysis
  -'budget_data.csv': The CSV file with the financial data
  -'financial_analysis.txt': The text file output with the final financial analysis results
  
  PyPoll:
  -'main.py': The file with the Python script for the election analysis
  -'election_data.csv': The CSV file with the election data
  -'election_results.txt': The text file output with the final election analysis results

# PyBank Instructions

  Dataset
  
  -File: 'budget_data.csv'
    - Columns: 'Date' & 'Profit/Losses'
    
  Analysis
  
  -The following calculations should be done by the script...
    1. Total months in the dataset
    2. Total profit/losses over the entire period
    3. Average change of the profit/losses over the entire period
    4. Greatest profit increases: the date as well as the amount
    5. Greatest profit decreases: the date as well as the amount

  Output
  
  The final results will print to the terminal and be saved in a new separate text file named 'financial_analysis.text' ...

Financial Analysis:
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

# PyPoll Instructions

  Dataset
  
  -File: 'election_data.csv'
    - Columns: 'Voter ID', 'County', 'Candidate'
    
  Analysis
  
  -The following calculations should be done by the script...
    1. Total numbers of casted votes
    2. The complete list of candidates who won votes
    3. The percentage of votes won by each candidate 
    4. Total number of votes received by each candidate
    5. The winning candidate who received the most votes

  Output
  
  The final results will print to the terminal and be saved in a new separate text file named 'election_results.text' ...

Election Results:
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------



# References 

# PyPoll/main.py: formatting Ln 40 & 52
Craven, P. V. (2017). Program arcade games with python and pygame. Program Arcade Games With Python And Pygame. http://programarcadegames.com/index.php?chapter=formatting&lang=en 

# PyPoll & PyBank/main.py: results to text file Ln 46-55 & Ln 53-60 
EdEx. (2024). Xpert Learning Assistant. 

# PyPoll & PyBank/main.py: += method Ln 19 & 26 & Ln 23 & 25
Gallagher, J. (2023, December 1). Python += operator: A guide. Career Karma. https://careerkarma.com/blog/python-operator/ 

# PyPoll/main.py: .get function Ln 32
GeeksforGeeks. (2024, August 1). Python dictionary GET() method. GeeksforGeeks. https://www.geeksforgeeks.org/python-dictionary-get-method/ 
