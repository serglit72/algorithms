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
senders = []
recievers = []
telemarks =[]

for text in texts:
    senders.append(text[0])
    recievers.append(text[1])

for row in calls:
    senders.append(row[0])
    recievers.append(row[1])
    
sendrs = sorted(set(senders))
recvrs = sorted(set(recievers))

print(len(sendrs))
for each in sendrs:
    
    if  each not in recvrs:
        telemarks.append(each)
print("These numbers could be telemarketers: ")
for item in telemarks:
    print(item)


""" 
Big O calculation (worst case):

O == 2n + 2n log n + n^2 = n^2  ,
 even We have n log(n) by  sort() operation we have to check each item from list A 
 and compare it with each item in list B , so n*n = n^2 the worst case. 


"""