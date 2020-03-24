"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as t:
    reader = csv.reader(t)
    texts = list(reader)

with open('calls.csv', 'r') as c:
    reader = csv.reader(c)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
if len(calls) !=0:
    phone_numbers = set()   
   

 # counting unique numbers from incoming and outgoing callers lists into the set:     
    for row in calls:
        phone_numbers.add(row[0])
        phone_numbers.add(row[1])
 
 # counting unique numbers from incoming and outgoing texters lists into the same set:
    for row in texts:
        phone_numbers.add(row[0])
        phone_numbers.add(row[1]) 
    
    
    print("There are {} different telephone numbers in the records.".format(len(phone_numbers)))
