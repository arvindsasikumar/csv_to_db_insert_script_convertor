import csv

with open('abc.csv', newline='') as f: #read input csv file
    reader = csv.reader(f)
    data = list(reader)
    
is_header_present = True #if input file has a header row
    
if (is_header_present):
    header_values = data.pop(0) #remove header row

ignore_col_set = set([5]) #columns in the input file to ignore
num_col_set = set([6]) #columns in the input file that are numerical
query = ''

for rows in data: #construct individual lines
    for i in range(0,len(rows)):
        if (i+1 not in num_col_set):
            rows[i] = '\'' + rows[i] + '\''
    for i in range(0,len(rows)):
        if (i+1 in ignore_col_set):
                del rows[i]
    query += '(' + ','.join(rows) + '),\n'

query = query[:-2] #removing unwanted final newline and comma
print(query)
