
#PyPoll Challenge

#import library
import csv
import os

#create path to input the file
csvpath=os.path.join('Resources', 'election_data.csv')

#create empty lists for the data
total_charles_votes=[]
total_diana_votes=[]
total_raymon_votes=[]

#create variables
total_votes= 0  
charles_votes=1
diana_votes=1
raymon_votes=1

#open the csv file
with open(csvpath) as pypoll_file:
    csvreader=csv.reader(pypoll_file, delimiter= ',')

    #Set up the header row
    header=next(csvreader) 

    for row in csvreader:
        #count up all the votes
        total_votes=total_votes +1

        #determine who was voted for 
        if row[2]== "Charles Casper Stockham":
            charles_votes=charles_votes + 1
            total_charles_votes.append(charles_votes)
        elif row[2]== "Diana DeGette":
             diana_votes=diana_votes+1
             total_diana_votes.append(diana_votes)
        elif row[2]== "Raymon Anthony Doane":
             raymon_votes=raymon_votes+1
             total_raymon_votes.append(raymon_votes)

    print("Election Results:")
    print(f"Total Votes= {total_votes}")

    #count how many times charles was voted for       
    c_v=(len(total_charles_votes))

    #count how many times diana was voted for
    d_v=(len(total_diana_votes))
    
    #count how many times raymon was voted for
    r_v=(len(total_raymon_votes))

    #find the percentage of votes that charles received 
    charles_pecentage=len(total_charles_votes)/(total_votes) *100

    #find the percentage of votes that diana received
    diana_percentage=len(total_diana_votes)/(total_votes) *100

    #find the percentage of votes that raymond received
    raymon_percentage=len(total_raymon_votes)/(total_votes) *100

    #print out the results
    print(f"Charles Casper Stockham= {charles_pecentage}% with {c_v} votes")
    print(f"Diana DeGette= {diana_percentage}% with {d_v} votes")
    print(f"Raymon Anthony Doane= {raymon_percentage}% with {r_v} votes")

    #Find out who is the winner
    if (charles_pecentage> diana_percentage) and (charles_pecentage>raymon_percentage):
        print("Charles is the winner!")
    elif (diana_percentage>charles_pecentage) and (diana_percentage>raymon_percentage):
        print("Diana is the winner!")
    elif (raymon_percentage>charles_pecentage) and (raymon_percentage>diana_percentage):
        print("Raymon is the winner!")
    else:
        print("it didnt work, fix your code!")

#create a text file that has the results from the analysis
analysis_path = os.path.join('Analysis', 'election_analysis.txt')   
with open(analysis_path, 'w') as txt_file:
     output=(
         f"Election Results:\n"
         f"Total Votes= {total_votes}\n"
         f"Charles Casper Stockham= {charles_pecentage}% with {c_v} votes\n"
         f"Diana DeGette= {diana_percentage}% with {d_v} votes\n"
         f"Raymon Anthony Doane= {raymon_percentage}% with {r_v} votes\n"
         f"Diana is the winner!"
        )
     
     print(output)
     txt_file.write(output)