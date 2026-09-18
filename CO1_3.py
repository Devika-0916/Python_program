#positive number
numbers=[-10,15,-3,8,0,22,-5]
positive_numbers=[x for x in numbers if x>0]
print("positive numbers:",positive_numbers)

#square of N numbers
n=5
squares=[x*x for x in range(1,n+1)]
print("squares of n numbers:",squares)

#form a list of vowels selected from a given word
word="python programming"
vowels=[char for char in word if char in "aeiousAEIOUS"]
print("Vowels in the word:",vowels)

#list ordinal value of each elemen t of a word
word="hello"
ordinal_values=[ord(char) for char in word]
print("Ordinal values:",ordinal_values)