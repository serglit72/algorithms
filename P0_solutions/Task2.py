"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
if len(calls) !=0:
    max_duration = 0
    for row in calls:
        
        if int(row[3])>max_duration:
            max_duration = int(row[3])
            phone_number_in = row[0]
            phone_number_out = row[1]
      
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_number_in,max_duration))

""" 
Big O calculation (worst case):

O == 2n  => n , because of linear dependency of the lists length. We have 2 lists by n items . 


"""