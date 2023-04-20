#Read a string from STDIN 
#Determine the frequency of each vowel in the string
#Determine the total number of vowels

sentence = input("Sentence: ")

total = 0

for v in "aeiou":
    frequency = sentence.lower().count(v)
    total += frequency
    print(f'{v} --> {frequency}')
    
print(f'Sentence has {total} vowels' )