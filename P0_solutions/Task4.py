"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order 
with no duplicates.
"""
texters = set()
callers = set()
telemarks = set()

# filtering all texting mobile numbers -"texters" group (not telemarketers)
for text in texts:
    texters.add(text[0])
    texters.add(text[1])

# filtering all recieving phone numbers (not telemarketers) and joining them to the texters group 

for row in calls:
    texters.add(row[1])
# for each callers from outcome calls list we check if the number is NOT in "texter's" list
for row in calls:
    if row[0] not in texters:
        telemarks.add(row[0])
    
telemarketers = sorted(telemarks)

print("These numbers could be telemarketers: ")
for each in telemarketers:
    print(each)
