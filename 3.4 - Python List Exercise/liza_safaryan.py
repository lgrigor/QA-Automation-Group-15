#Exercise 1
list1 = [100, 200, 300, 400, 500]
list1 = list1[::-1]
print("Exercise 1", list1)


#Exercise 2
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(1, 7000)
print("Exercise 2", list1)
 

# Exercise 3
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print("Exercise 3", list1)


# Exercise 4
list1 = [5, 10, 15, 20, 25, 50, 20]
i = list1.index(20)
list1.remove(20)
list1.insert(i, 200)
print("Exercise 4", list1)
