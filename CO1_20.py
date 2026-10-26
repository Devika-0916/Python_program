numbers=[int(x)for x in input("Enter integers(space-separated):").split()]
odd_numbers=[x for x in numbers if x%2!=0]
print("List without even numbers:",odd_numbers)
