import re

sample_file = 'sample1.txt'
f = open(sample_file, 'r')
data = f.readlines()

for row in data:
    if row.strip() == 'Employer':
        row_num = data.index(row)
        break

print data[row_num-2]
