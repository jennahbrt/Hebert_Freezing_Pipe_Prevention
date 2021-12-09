"""
multi line comment
"""

import sys
#import csv module 
import csv
infile = open(sys.argv[1])
reader = csv.reader(infile)
headings = []
rows = []
#min, max, and sum are python keywords 
# dont use them as vars 
maxTemp = 0
minTemp = 99
averageTemp = 0

#extract field 2 for temp value
#list element 2
#array element 1 (index at 0)
headings = reader.next()
#print "Headings are:", headings
for line in reader:
    rows.append(float(line[1]))
    if float(line[1]) > maxTemp:
        maxTemp = float(line[1])
    if float(line[1]) < minTemp:
        minTemp = float(line[1])
Total = sum(rows)
averageTemp = Total/len(rows)

print "Temperature Report"
print "Average: ", averageTemp
print "Min: ", minTemp
print "Max: ", maxTemp
