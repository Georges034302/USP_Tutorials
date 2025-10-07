# Read day and month from STDIN
# Determine and show total days from January first until this day

days = [31,28,31,30,31,30,31,31,30,31,30,31]

day = int(input("Day = "))
month = int(input("Month = "))

i = 0
total = 0
while i < month-1:
    total += days[i]
    i +=1
total += day

print(f'Total days = {total}')