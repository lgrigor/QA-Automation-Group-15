#Exercise1.
list_1 = [1,2,3,4,5]
list_1.reverse()
print(list_1)

#Exercise2.
list_1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list_1[2][2].append(7000)
print(list_1)

#Exercise3.
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
letters = ["h","i","j"]
list1[2][1][2].extend(letters)
print(list1)

#Exercise4.
list1 = [1,34,55,32,20,54,74,20,60]
print(20 in list1)
index=list1.index(20)
list1[index]=200
print(list1)