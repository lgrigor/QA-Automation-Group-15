#In Python, Strings are arrays of bytes representing Unicode characters


Name = input("Type your Text: ")
Name1=Name[0:len(Name)//2].upper()
Name2=Name[len(Name)//2:].lower()
print(Name1)
print(Name2)
print(Name1+Name2)

#or
Name = input("Type your Text: ")

print(Name[0:len(Name)//2].upper()+Name[len(Name)//2:].lower())








