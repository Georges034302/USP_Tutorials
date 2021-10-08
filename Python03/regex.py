#!/bin/env python3

import re

txt = '''01- Welcome to USP 32547
         This is Week 08
         Session Spr 2021'''

x = re.match("[0-9]{2}",txt)
print(x)

x = re.search("\d{2}$",txt)
print(x)

x = re.search("[A-Z]{3}",txt)
print(x)
print(x.span())
print(x.group())

x = re.findall("\d{2}",txt)
print(x)

x = re.findall("[A-Z]",txt)
print(x)

x = re.sub("USP","Python",txt)
print(x)

x = re.sub("\s",".",txt)
print(x)
