#!/bin/env python3

import re 

s = 'USP python3 - spring 2024'

print(re.search('p',s))
print(re.findall('p',s))
print(re.findall('p',s,flags=re.IGNORECASE))

# Replace all digits with _ 
print(re.sub('\\d','_',s))
