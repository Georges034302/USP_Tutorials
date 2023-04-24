import re 

#  /    this is slash
#  \    escape  (nullifies the effect of the next character)
#  ?    hook    (zero or one character)
#  *    star    (zero or many characters)
#  +    plus    (one or many characters)
#  \d   one digit
# [0-9] one digit
#  ^    beginning of a line
#  $    end of a line
#  \s   whitespace
#  ( )  whitespace
# {m,n} quantifier (means numbers between m and n) 
# [a-z] lower cases
# [A-Z] upper cases

txt = \
"""
^Day05: SysAdmin, Debugging, RegEX in Python
1 - Lesson 1: Using re module from python library
2 - Lesson 2: SysAdmin commands from os Module
OS Module from Python has over 100 functions
3 - Lesson 3: Debugging python scripts$
^ NOTE: Today we will discuss #10 challenge exercises 
25/03/2022 
"""

obj = re.search("\^",txt)
print(obj)

obj = re.search("\$",txt)
print(obj)

obj = re.search("\d{2,3}",txt)
print(obj)

obj = re.search("\d{3,}",txt)
print(obj)

objList = re.findall("\d{2}",txt)
print(objList)

objList = re.findall("\d{2,3}",txt)
print(objList)

objList = re.findall("[A-Z]",txt)
print(objList)

objList = re.findall("\^",txt)
print(objList)

objList = re.findall("\^|#",txt)    #match ^ or #
print(objList)

objList = re.findall("[\^#]",txt)   #match ^ or #
print(objList)

objList = re.findall("\^.*#",txt)   #match ^ and #
print(objList)

replace = re.sub('python','JAVA',txt,flags=re.IGNORECASE)
print(replace)

