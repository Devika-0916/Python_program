word=input("Enter a String:")
length=len(word)


if length >  2:
    if word[-3:] == "ing":
       print(word + "ly")
    else:
       print(word + "ing")
else:
   print("Invalid Format") 