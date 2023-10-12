#!/bin/python3
import re
s = 'JAva 17 is better thAn Python 3.11'
result = re.match('[A-Z]',s)
print(result)
result = re.search('\d{2}',s)
print(result)
result = re.findall('[0-9]{2}',s)
print(result)

text = re.sub('\s','_',s)
print(text)
text = re.sub('a','@',s,flags=re.IGNORECASE)
print(text)
