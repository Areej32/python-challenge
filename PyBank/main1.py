import os
import csv


months=[]
revenue=[]
revenue_change=[]

fPath = os.path.join("budget_data.csv")
with open(fPath,'r') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     next (csvreader)

     for row in csvreader:
         months.append(row[0])
         revenue.append(int(row[1]))

#total number of months(I can use len function or set function)
         T_months=set(months)
# total net amount of "Profit/Losses" 
# (i can do sum function or creat for loop)        
         net=sum(revenue)

# print results for the 1st and 2nd task
         print ('Financial Analysis')
         print('________________________________')
         print('Total Months:'+str(len(T_months)))
         print('Total net amount: $'+str(net))

# __________________________________________________________________
  # avg_net_change=
  # max_net=
  # min_net=

  # To find these values I have to creat a for loop that will itrate
  #  the revenue 
    
# average change in "Profit/Losses"(=sum/len)

for i in range(0,len(revenue)-1):
    revenue_change.append(int(revenue[i+1])-int(revenue[i]))
    avg_net_change=round(sum(revenue_change)/len(revenue_change),2)

 # greatest increase in profits (date and amount)(max function)
    max_net=max(revenue_change)
        # associate date for the max
    max_date=months[revenue_change.index(max_net)]
# greatest decrease in losses (date and amount) (min function)
    min_net=min(revenue_change)
    min_date=months[revenue_change.index(min_net)]

#printing the results
    print("Averege revenue change:$"+str(avg_net_change))
    print('Greatest increase in revenue:'+ max_date+("$")+ str(max_net))
    print('Greatest decrease in revenue:'+ min_date+("$")+ str(min_net))

# _____________________________________________________________________

# I have to print all results together in a text file

with open("Financial_analysis.txt", "w") as text_file:
     print('Financial Analysis\n---------------------\nTotal Months:' +" "+
      str(len(T_months)) +
      '\nTotal net amount: $'+" "+
      str(net) +'\nAverage  Change: $'+" "+
      str(avg_net_change) +'\nGreatest Increase in Profits:' +" "+
       str(max_date) +" "+ '($' + str(max_net) + ')' +
        '\nGreatest Decrease in Profits:' +" "+ str(min_date) +" "+
        '($' + str(min_net) + ')', file = text_file)
    
 






       













