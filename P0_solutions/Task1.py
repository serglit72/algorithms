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
    phone_numbers_in = []   
    phone_numbers_out = [] 
    total = []  
    for row in calls:
        phone_numbers_in.append(row[0])
        phone_numbers_out.append(row[1])
    total = set(phone_numbers_in+phone_numbers_out)

    print("There are {} different telephone numbers in the records.".format(len(total)))

""" 
Big O calculation (worst case):

O == 2n + n = 3n => n , because of linear dependency of the lists length. We have 2 lists by n items and "set" operation O(n). 


"""
