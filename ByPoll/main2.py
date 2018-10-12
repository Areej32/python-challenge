import os
import csv


election_Path = os.path.join("election_data.csv")
with open(election_Path,'r') as csvfile:
     election_csvreader = csv.reader(csvfile, delimiter=',')
     next (election_csvreader)

     Election=list(election_csvreader)
     Election_head=Election[0]
     Election_data=Election[1:]


 # The total number of votes 

total=len(Election_data)
candidate_dict={}

for vote in Election_data:
    if vote[2] not in candidate_dict:
         candidate_dict[vote[2]]=1
    else:
         candidate_dict[vote[2]]+=1

 # * A complete list of candidates who received votes

         print(candidate_dict)

print('Election Results!')
print('_______________________________')
print(f'Total Votes: {total}')
print('_______________________________')
       
# * The percentage of votes each candidate won
for key in candidate_dict:
    print(f'{key}: {round((candidate_dict[key]/total)*100,2)}% ({candidate_dict[key]})')

print('________________________________')

# * The total number of votes each candidate won
winner = max(candidate_dict, key=candidate_dict.get)

# * The winner of the election based on popular vote.
print(f'Winner is: {winner}')

#printing all results in Txt file
path2=os.path.join('Election_analysis.txt')
text=open(path2,'w')
text.write('```text\n')
text.write('Election Results!\n')
text.write('------------------\n')
text.write(f'Total Votes: {total}\n')
text.write('------------------\n')

for key in candidate_dict:

    text.write(f'{key}: {round((candidate_dict[key]/total)*100,2)}% ({candidate_dict[key]})\n')

text.write('------------------\n')
text.write(f'Winner is: {winner}\n')
text.write('````')
text.close()





