list1 = [100, 200, 300, 400, 500]
print(list1[::-1])

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].insert(2, 7000)
print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]
list1[2][1][2].extend(list2)
print(list1)

list1 = [5, 10, 15, 20, 25, 50, 20]
list2 = list1.index(20)
list1[list2]=200
print(list1)

