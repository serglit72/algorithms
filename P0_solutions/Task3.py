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
fixed_lines = []
fixed_lines_calls =[]
mobile_lines = []
telemark = ['140',]
all_codes = []
###### Part A ################
for row in calls:
  
  if row[0].startswith("9") or row[0].startswith("8") or row[0].startswith("7"):
    code = row[0][0:4]
    mobile_lines.append(code)
  elif row[1].startswith("9") or row[1].startswith("8") or row[1].startswith("7"):
    code = row[1][0:4]
    mobile_lines.append(code)
  elif row[0].startswith("(0") :
    if row[0].startswith("(080)") :
      fixed_lines_calls.append((row[0],row[1]))
      
    code = row[0].split(")")
    fixed_lines.append(code[0].strip("("))
  elif row[1].startswith("(0") :
    code = row[1].split(")")
    fixed_lines.append(code[0].strip("("))

all_codes = fixed_lines+mobile_lines+telemark
print("The numbers called by people in Bangalore have codes:")

sorted_list = sorted(set(all_codes))
for each in sorted_list:
  print(each)

##### Part B #########################

total_calls = len(fixed_lines_calls)
total_080_calls = 0

for each in fixed_lines_calls:
  if each[1].startswith("(080)"):
    total_080_calls +=1
print("{} percent of calls from fixed lines in Bangalore are calls \
 to other fixed lines in Bangalore.".format(total_080_calls/total_calls))

""" 
Big O calculation (worst case):

O == 6n + n log n =  n log(n)  , because of linear dependency of the lists length. We have 5 lists by n items and "set" operation O(n) and sort() operation n log(n). 


"""