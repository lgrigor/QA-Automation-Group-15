title = "Conversion of Temperature"
c = title.center(50, ' ')
print(c)
name = input("Please enter your name: ")
deg = float(input("Please enter the temperature in Celsius: "))
degree_sign = u"\N{DEGREE SIGN}"
f = (deg * 9 / 5) + 32
print(deg,degree_sign,"C", " is equal to ", f, degree_sign, "F", sep = "")
print("Thank you for your time " + name.capitalize() + "!")
input()