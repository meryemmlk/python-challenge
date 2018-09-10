import os
import csv

budget_csv = os.path.join("budget_data.csv")

with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total = 0
    count = 0
    max_inc = 0
    max_dec = 0
    averages = []
    imaxinc = ""
    imaxdec = ""
    x = 0
    y = 0
    change = 0
    
    # Loop through the data
    for row in csvreader:
        count += 1
        y = float(row[1])
        change = y-x
        
        if count > 1:
            averages.append(y-x)
            if change > max_inc:
                max_inc = change
                imaxinc = row[0]
            if change < max_dec:
                max_dec = change
                imaxdec = row[0]
        total += float(row[1])
        x = float(row[1]) 

    average_total = 0
    count_average = 0
    for ave in averages:
        average_total += float(ave)
        count_average +=1

    print(" ")
    print(" Financial Analysis")
    print("----------------------------")
    print("Total Months: {}".format(count))
    print("Total: ${:0.0f}".format(total))
    print("Average Change: ${:0.2f}".format(average_total/count_average))
    print("Greatest Increase in Profits: {} (${:0.0f})".format(imaxinc, max_inc))
    print("Greatest Decrease in Profits: {} (${:0.0f})".format(imaxdec, max_dec))

    output_file = os.path.join("budget_results.txt")
    with open(output_file, "w") as datafile:
        datafile.write("\n")
        datafile.write(" Financial Analysis\n")
        datafile.write("---------------------------\n")
        datafile.write("Total Months: {}\n".format(count))
        
        datafile.write("Total: ${:0.0f}\n".format(total))
        datafile.write("Average Change: ${:0.2f}\n".format(average_total/count_average))
        datafile.write("Greatest Increase in Profits: {} (${:0.0f})\n".format(imaxinc, max_inc))
        datafile.write("Greatest Decrease in Profits: {} (${:0.0f})\n".format(imaxdec, max_dec))
    
    
        