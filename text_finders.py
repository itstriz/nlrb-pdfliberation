import re

sample_file = 'sample1.txt'
f = open(sample_file, 'r')
data = f.readlines()

regex = re.compile(r'[A-z]*, [A-Z]{2}')
loc_info = regex.search(''.join(data))

print loc_info.group()
