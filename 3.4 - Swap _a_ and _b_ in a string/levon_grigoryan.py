# Write a program that takes a string as an input and replaces the letter "a" with "b", and the letter "b" with "a".
# Example:
#  * Sample Input: ab ra ca dab ra
#  * Sample Output: ba rb cb dba rb

# Using translation
print(input('Enter text: ').translate(str.maketrans('ab', 'ba')))

# Using replacements (more logical approach)
print(input('Enter text: ').replace('a', '%temp%').replace('b', 'a').replace('%temp%', 'b'))
