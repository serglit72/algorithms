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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
codes = set()
fixed_lines_calls = 0
bangalores_caller = 0
###### Part A ################
for row in calls:

# looking up for all callers form Bangalore:  
    if row[0].startswith("(080)"):
      bangalores_caller += 1
      #filtering for all mobile lines recievers of the calls by "area code 080" callers
      if row[1].startswith("7") or row[1].startswith("8") or row[1].startswith("9"):
        code = row[1][0:4]
        codes.add(code)
# filtering for all fixed lines recievers of the calls by "area code 080" callers
      elif row[1].startswith("("):
        code = row[1][1:(row[1].find(')'))]
        fixed_lines_calls += 1 #additional counting of calls for Task2
        codes.add(code)
        
       


print("The numbers called by people in Bangalore have codes:")
for each in sorted(codes):
  print(each)
    
##### Part B #########################


print("{:.2%} of calls from fixed lines in Bangalore are calls \
 to other fixed lines in Bangalore.".format(fixed_lines_calls/bangalores_caller))

""" 
Big O calculation (worst case):

O == n + n log n =  n log(n)  , because of linear dependency of the lists length. \
   We have 1 list by n items and "set" operation O(n) and sort() operation n log(n). 

O(nlog(n))
"""
