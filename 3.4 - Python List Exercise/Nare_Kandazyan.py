list=[100,200,300,400,500]
list.reverse()
print(list)

list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list[2][2].append(7000)
print(list)

list =  ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list[2][1][2].extend(["h","i","j"])
print(list)

list = [5, 10, 15, 20, 25, 50, 20]
if 20 in list: list.replace(20,200)
print(list)