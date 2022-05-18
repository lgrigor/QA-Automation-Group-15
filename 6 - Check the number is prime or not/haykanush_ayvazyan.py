
def prime_number(number):
    if number >1:
        for i in range(2,number):
            if number%i==0:
                return False
        else:
            return True
    else:
        return False
print(prime_number(149))
        



        



   
        




#Write a Python function that takes a number as an argument and returns True if the number is a prime, otherwise False.
