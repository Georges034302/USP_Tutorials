#!/bin/python3
import re 

s = 'JAVA 17 is better than Python 3.11'

print(re.match('[A-Z]',s))
print(re.search('\d{2}',s))
print(re.findall('[0-9]{2}',s))

print(re.sub('\s','_',s))
print(re.sub('a','@',s,flags=re.IGNORECASE))
