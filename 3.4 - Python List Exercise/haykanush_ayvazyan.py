#Exercise 1
list1 = [5, 10, 15, 20, 25, 50, 20]
print(20 in list1)
index=list1.index(20)
list1[index]=200
print(list1)

#Exercise 2
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#Exercise 3
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].extend(["h","i","j"])
print(list1)

#Exercise 4
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)














