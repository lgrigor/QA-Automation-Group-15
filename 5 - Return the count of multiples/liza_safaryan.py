a=input()
x=(a).split(',')
mof3=[]
mof5=[]
mof3and5=[]
for y in x:
    if int(y) % 3 == 0:
        mof3.append(y)
    if int(y) % 5 == 0:
        mof5.append(y)
    if int(y) % 3 == 0 and int(y) % 5 == 0:
        mof3and5.append(y)

print('Multiples of three: ', len(mof3), '\nMultiples of five: ', len(mof5), '\nMultiples of three and five: ', len(mof3and5))