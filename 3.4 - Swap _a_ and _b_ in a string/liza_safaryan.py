#Write a program that takes a string as an input and replaces the letter "a" with "b", and the letter "b" with "a".
#Example:
#* Sample Input: a ra ca dab ra
#* Sample Output: ba rb cb dba rb
print("Please enter your text here (numbers are strictly forbidden", "\U0001F605", "): ", end = "")
text = input()
text1 = text.replace("a", "1", len(text)).replace("b", "2", len(text))
print("\033[95m", "\033[1m", text1.replace("1" , "b", len(text1)).replace("2", "a", len(text1)), "\033[0m")



