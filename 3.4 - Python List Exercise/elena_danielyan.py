#Exercise1_Reverse List
users_list = list(input("Enter elements of a list: "))
print(users_list[::-1])

#Exercise2_Add_Item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#Exercise3_Extend_Sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 =  ["h", "i", "j"]
list1[2][1][2].extend(list2)
print(list1)

#Exercise4_Find_and_Replace
list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 200
print(list1)
