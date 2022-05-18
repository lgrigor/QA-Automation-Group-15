# Exercise 1: Reverse a given list in Python
# Version 1

list1 = [100, 200, 300, 400, 500]
print(list1[::-1])

#version 2
list1 = [100, 200, 300, 400, 500]

#list1.reverse()

print(list1.reverse())

#Exercise 2: Add item 7000 after 6000 in the following Python List
array_list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

array_list1[2][2].insert(2, 7000 )

print(array_list1)


#Exercise 3: Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list

main_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

main_list[2][1][2].extend(sub_list)

print(main_list)

#Exercise 4: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

last_list = [5, 10, 15, 20, 25, 50, 20]

last_list[last_list.index(20)] = 200

print(last_list)
