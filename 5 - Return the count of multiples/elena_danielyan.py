x = tuple([int(i) for i in input("Enter values: ").split()])
count3 = 0
for i in x:
    if i % 3 == 0:
        count3 += 1
print("Multiples of three:", count3)
count5 = 0
for i in x:
    if i % 5 == 0:
        count5 +=1
print("Multiples of five:", count5)
count3_5 = 0
for i in x:
    if i % 3 == 0 and i % 5 == 0:
        count3_5 += 1
print("Multiples of three and five:", count3_5)




