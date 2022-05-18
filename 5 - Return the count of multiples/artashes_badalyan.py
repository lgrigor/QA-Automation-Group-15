mylist = [1,5,8,9,13,24,25,31,35,46,60,81,84,10,90,12]
newlist1 = [x for x in mylist if x%3 == 0]
print("Multiples of three: ",len(newlist1))
newlist2 = [x for x in mylist if x%5 == 0]
print("Multiples of five:  ",len(newlist2))
newlist3 = [x for x in mylist if x%5 == 0 and x%3 == 0]
print("Multiples of five and three:  ",len(newlist3))