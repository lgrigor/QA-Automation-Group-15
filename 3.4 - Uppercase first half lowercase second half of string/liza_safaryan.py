text = input("Please enter your text here: " )
first_half = len(text)//2
print(text[:first_half].upper() + text[first_half:].lower())