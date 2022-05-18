a=(78, 90, 65, 35, 72, 28, 82, 64, 33, 45, 38, 40, 81, 1, 75, 34, 16, 20, 98, 7, 21)
result = 0
result1=0
result2=0

for i in a:
    if i%3 == 0:
        result += a.count(i)
    if i % 5 ==0:
        result+=a.count(i)
    if i%3 ==0 and i%5==0:
        result2+=a.count(i)
print(result)
print(result1)
print(result2)


