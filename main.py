import os
import csv

#Create some variables to store vote counts

khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

#Open the CSV file

csvpath = os.path.join("votes.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Add 1 vote to the counter each time a name is found

    for row in csvreader:
        if row[2] == "Khan":
            khan_count += 1
        elif row[2] == "Correy":
            correy_count += 1
        elif row[2] == "Li":
            li_count += 1
        elif row[2] == "O'Tooley":
            otooley_count += 1

#Calculate the total count and the percentages

total_count = khan_count + correy_count + li_count + otooley_count
khan_percentage = khan_count / total_count * 100
correy_percentage = correy_count / total_count * 100
li_percentage = li_count / total_count * 100
otooley_percentage = otooley_count / total_count * 100

#Print the results

print("Election Results:")
print("---------------------------------")
print(f"Total Votes: {total_count}")
print("---------------------------------")
print(f"Kahn's Total: {round(khan_percentage)}.000% ({khan_count})")
print(f"Correy's Total: {round(correy_percentage)}.000% ({correy_count})")
print(f"Li's Total: {round(li_percentage)}.000% ({li_count})")
print(f"O'Tooley's Total: {round(otooley_percentage)}.000% ({otooley_count}")
print("---------------------------------")

if khan_count > correy_count and li_count and otooley_count:
    print("The Winner is: Kahn")

if correy_count > khan_count and li_count and otooley_count:
    print("The Winner is: Correy")

if li_count > khan_count and li_count and otooley_count:
    print("The Winner is: Li")

if otooley_count > khan_count and correy_count and li_count:
    print("The Winner is: O'Tooley")
print("---------------------------------")

#Generate a txt document with the same info

print("Election Results:", file=open("Results.txt", "a"))
print("---------------------------------", file=open("Results.txt", "a"))
print(f"Total Votes: {total_count}", file=open("Results.txt", "a"))
print("---------------------------------", file=open("Results.txt", "a"))
print(f"Kahn's Total: {round(khan_percentage)}.000% ({khan_count})", file=open("Results.txt", "a"))
print(f"Correy's Total: {round(correy_percentage)}.000% ({correy_count})", file=open("Results.txt", "a"))
print(f"Li's Total: {round(li_percentage)}.000% ({li_count})", file=open("Results.txt", "a"))
print(f"O'Tooley's Total: {round(otooley_percentage)}.000% ({otooley_count})", file=open("Results.txt", "a"))
print("---------------------------------", file=open("Results.txt", "a"))

if khan_count > correy_count and li_count and otooley_count:
    print("The Winner is: Kahn", file=open("Results.txt", "a"))

if correy_count > khan_count and li_count and otooley_count:
    print("The Winner is: Correy", file=open("Results.txt", "a"))

if li_count > khan_count and li_count and otooley_count:
    print("The Winner is: Li", file=open("Results.txt", "a"))

if otooley_count > khan_count and correy_count and li_count:
    print("The Winner is: O'Tooley", file=open("Results.txt", "a"))
print("---------------------------------", file=open("Results.txt", "a"))