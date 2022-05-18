s = input("Enter your text: " )        
L = len(s) // 2
a = s[:L].upper()
b = s[L:].lower()
print(a + b)

