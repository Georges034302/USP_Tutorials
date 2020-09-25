#!/bin/env python
age = 35
name = "Tom"

print("Welcome "+name, end=" ----- ")
print("Your age is: "+str(age))

savings = 150
loan = 250
print()
print("Old Style---------------------------------------------------------------")
#Old Method
print ("%s bank statement: savings $%d and owing $%d"%("Tom",savings,loan))
print ("%10s bank statement: savings $%10d and owing $%10d"%("Tom",savings,loan))
print ("%-10s bank statement: savings $%-10d and owing $%-10d"%("Tom",savings,loan))
print ("%-10s bank statement: savings $%.2f and owing $%.3f"%("Tom",savings,loan))
print ("%-10s bank statement: savings $%10.2f and owing $%10.3f"%("Tom",savings,loan))
print ("%-10s bank statement: savings $%-10.2f and owing $%-10.3f"%("Tom",savings,loan))
print()

print("New Style:---------------------------------------------------------------")
txt1 = "{} bank statement: savings ${} and owing ${}"
print(txt1.format(name,savings,loan))
txt1 = "{:<10} bank statement: savings ${:<10} and owing ${:<5}"
print(txt1.format(name,savings,loan))
txt1 = "{:*<10} bank statement: savings ${:_<10} and owing ${:-<5}"
print(txt1.format(name,savings,loan))
txt1 = "{:>10} bank statement: savings ${:>10} and owing ${:>10}"
print(txt1.format(name,savings,loan))
txt1 = "{:*>10} bank statement: savings ${:_>10} and owing ${:_>10}"
print(txt1.format(name,savings,loan))
txt1 = "{:^10} bank statement: savings ${:^10} and owing ${:^10}"
print(txt1.format(name,savings,loan))
txt1 = "{:*^10} bank statement: savings ${:-^10} and owing ${:=^10}"
print(txt1.format(name,savings,loan))
txt1 = "{0} bank statement: savings ${2} and owing ${1}"
print(txt1.format(name,savings,loan))
txt1 = "{0:*>10} bank statement: savings ${2:_>10} and owing ${1:-<10}"
print(txt1.format(name,savings,loan))
print()
print("New Style:Decimal formatting---------------------------------------------")
txt2 = "{} bank statement: savings ${:.2f} and owing ${:.4f}"
print(txt2.format(name,savings,loan))
txt2 = "{0} bank statement: savings ${2:.2f} and owing ${1:.4f}"
print(txt2.format(name,savings,loan))
txt2 = "{0} bank statement: savings ${2:10.2f} and owing ${1:10.4f}"
print(txt2.format(name,savings,loan))
txt2 = "{0} bank statement: savings ${2:=>10.2f} and owing ${1:-<10.4f}"
print(txt2.format(name,savings,loan))
print()
print("New Style:Varibale formatting--------------------------------------------")
txt3 = name+" bank statement: savings ${savings} and owing ${loan}"
print(txt3.format(savings=300,loan=500))
txt3 = name+" bank statement: savings ${savings:>10} and owing ${loan:<10}"
print(txt3.format(savings=300,loan=500))
txt3 = name+" bank statement: savings ${savings:=>10} and owing ${loan:*<10}"
print(txt3.format(savings=300,loan=500))
txt3 = name+" bank statement: savings ${savings:.2f} and owing ${loan:.4f}"
print(txt3.format(savings=300,loan=500))
txt3 = name+" bank statement: savings ${savings:->10.2f} and owing ${loan:_<10.4f}"
print(txt3.format(savings=300,loan=500))



