a=input("Write Your Text: ")
k=a.lower()
print(k)
b=k.replace("ab","*")
c=b.replace("ba","$")
d=c.replace("a","@")
e=d.replace("b","a")
f=e.replace("@","b")
g=f.replace("*","ba")
h=g.replace("$","ab")
print(a)
print(b)
print(d)
print(e)
print(f)
print(g)
print(h)

#Sample Output:   ba rb cb dba rb






