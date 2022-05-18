#Exercise 1:
list1 = [100, 200, 300, 400, 500]
print(list1[: : -1])

#Exercise 2:
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2, 7000)
print(list1)

#Exercise 3:
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]
list1[2][1][2].extend(list2)
print(list1)


#Exercise 4:
list1 = [5, 10, 15, 20, 25, 50, 20]
a = int(input())
i = list1.index(a)
list1.pop(i)
list1.insert(i, 200)
print(list1)


