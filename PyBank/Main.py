import os
import csv

Budget_data = os.path.join("Resources", "Budget_data.csv")

#Reading data from the file budget_data.csv
with open(Budget_data, 'r', newline='') as csvfile:    
    
    csvreader = csv.reader(csvfile, delimiter=',')
    #Reading header data in csv_header
    csv_header = next(csvreader)

    #Initializing values of the variables and lists
    dates = []
    total_rev = 0
    maxProfit = 0
    minProfit = 0
    
    #Looping through each data record in the file
    for row in csvreader:
        dates.append(row[0])
        #Summing up the revenue for each month
        total_rev += int(row[1])

        #Calculating the maximum profit
        if(maxProfit<int(row[1])):
            maxProfit = int(row[1])
            maxProfitMonth = row[0]
        
        #Calculating the minimum profit or maximum loss
        if(minProfit>int(row[1])):
            minProfit = int(row[1])
            minProfitMonth = row[0]
    
    #Printing results in Git Bash
    print("\nFinancial Analysis\n-----------------------------------------------")
    print(f"Total Month: {len(dates)}")
    print(f"Total Revenue : ${total_rev}")
    print(f"Average Change : ${round(total_rev/len(dates),2)}")
    print(f"Greatest Increase in Profits : {maxProfitMonth} ({maxProfit})")
    print(f"Greatest Decrease in Profits : {minProfitMonth} ({minProfit})")

file = open('Financial_Analysis.txt','w')

#Writing outputResults in the file (Financial_Analysis)
file.write("Financial Analysis")
file.write("\n-----------------------------------------------")
file.write("\nTotal Month: " + str(len(dates)))
file.write("\nTotal Revenue : $" + str(total_rev))
file.write("\nAverage Change : $" + str(round(total_rev/len(dates),2)))
file.write("\nGreatest Increase in Profits : " + str(maxProfitMonth) + " (" + str(maxProfit) + ")")
file.write("\nGreatest Decrease in Profits : " + str(minProfitMonth) + " (" + str(minProfit) + ")")

file.close()


  


