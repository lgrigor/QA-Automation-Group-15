string = input("Write down a phrase. ")
print(string[0:len(string)//2].upper() + string[len(string)//2:].lower())