x = input("Enter any text")
stringlength = len(x)
lowerstring = x.lower()
upperstring = x.upper()
cutlen = stringlength - (stringlength // 2)
answer = upperstring[:cutlen] + lowerstring[cutlen:]
print(answer)