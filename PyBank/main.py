
import os
import csv

#collect data from folder
BudDa = os.path.join(".","Resources","budget_data.csv")

#read csv file
with open(BudDa, newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

  #total number of months
    next(csv_reader)
    data = list(csv_reader)
    row_count = len(data)

  #profit/losses
    total = 0
    for i in range(0, row_count): 
        total = total + int(data[i][1]) 

  #average profit/losses  
    num1 = 0
    num2 = int(data[0][1])
    diff = 0
    difflist = list()
    for j in range(1, row_count):
        num1 = int(data[j][1])
        diff = num1 - num2
        difflist.append(diff)
        num2 = int(data[j][1])
    avgProLos = round(sum(difflist)/len(difflist),2)

  #greatest increase in profits
    incPro = max(difflist)
    MAXincPro = difflist.index(incPro)+1
    
  #greatest decrease in profits
    decPro = min(difflist)
    MINdecPro = difflist.index(decPro)+1

  #terminal print
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total:,}")
    print(f"Average Change: ${avgProLos:,}")
    print(f"Greatest Increase in Profits: {data[MAXincPro][0]} (${incPro:,})")
    print(f"Greatest Decrease in Profits: {data[MINdecPro][0]} (${decPro:,})")

  #txt print
    print("Financial Analysis", file=open("PyBank.txt", "a"))
    print("----------------------------", file=open("PyBank.txt", "a"))
    print(f"Total Months: {row_count}", file=open("PyBank.txt", "a"))
    print(f"Total: ${total:,}", file=open("PyBank.txt", "a"))
    print(f"Average Change: ${avgProLos:,}", file=open("PyBank.txt", "a"))
    print(f"Greatest Increase in Profits: {data[MAXincPro][0]} (${incPro:,})", file=open("PyBank.txt", "a"))
    print(f"Greatest Decrease in Profits: {data[MINdecPro][0]} (${decPro:,})", file=open("PyBank.txt", "a"))