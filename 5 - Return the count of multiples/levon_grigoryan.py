multiples_of_3 = multiples_of_5 = multiples_of_3_and_5 = 0
the_sequence = (78, 90, 65, 35, 72, 28, 82, 64, 33, 45, 38, 40, 81, 1, 75, 34, 16, 20, 98, 7, 21)

for number in the_sequence:
    multiples_of_3 += 1 if number % 3  == 0 else 0
    multiples_of_5 += 1 if number % 5  == 0 else 0
    multiples_of_3_and_5 += 1 if number % 15 == 0 else 0
        
print(f"Multiples of tree : {multiples_of_3}")
print(f"Multiples of five : {multiples_of_5}")
print(f"Multiples of tree and five : {multiples_of_3_and_5}")
