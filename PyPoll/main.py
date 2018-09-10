import os
import csv


election_csv = os.path.join("election_data.csv")


with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)


    total = 0
    
    candidates = []
    
    votecounts = {}

    # Loop through the data
    
    for row in csvreader:
        total += 1
        candidate = row[2]
        if (candidate in candidates):
            votecounts[candidate] += 1

        else:
            candidates.append(candidate)
            votecounts[candidate] = 1

    print(" ")
    print(" Election Results")
    print("----------------------------")
    print(" Total Votes: ", total)
    print("----------------------------")
    maxname = ""
    maxcount = 0
    for key, value in votecounts.items() :
        if value > maxcount:
            maxcount = value
            maxname = key
        print (" {0:10} : {1:3.3f}% ( {2:0.0f} )".format(key, value/total*100, value))
    print("----------------------------")
    print(" Winner : ",maxname)
    print("----------------------------")


    output_file = os.path.join("election_results.txt")
    with open(output_file, "w") as datafile:
        datafile.write("\n")
        datafile.write(" Election Results\n")
        datafile.write("---------------------------\n")
        datafile.write(" Total Votes: {}".format(total))
        datafile.write("\n---------------------------\n")
        maxname = ""
        maxcount = 0
        for key, value in votecounts.items() :
            if value > maxcount:
                maxcount = value
                maxname = key
            datafile.write(" {0:10} : {1:3.3f}% ( {2:0.0f} ) \n".format(key, value/total*100, value))
        datafile.write("---------------------------\n")
        datafile.write(" Winner : {}".format(maxname))
        datafile.write("\n---------------------------\n")

    
        