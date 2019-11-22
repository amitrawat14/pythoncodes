## Script find the unique lines in the file, i.e We have network flows and we need uniques flows source/destination/port in thousands 
## of flows . 

## Script find the unique lines in the file, 

import csv
reader = csv.reader(open("log.csv"))
reader = list(reader)
duplicate = []
for line in reader[1:]:
    if line not in duplicate:
       print(line)
       duplicate.append(line)


print("Tola line scanned" , len(reader))
print("Total Unique line found",len(duplicate))

---

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
for index,line in enumerate(duplicate):
    print(index,line)
    outputWriter.writerow(line)

outputFile.close()



