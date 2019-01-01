l = [1,2,3,4,5,6,7,8,9]
print(l)
print(id(l))
print(id(l[0]))
print(id(l[1]))
print(id(l[2]))
print(id(l[3]))
l.remove(1)
print(l)
print(id(l))
print(id(l[0]))
l = [0]
for i in range(1,1000):
    print(l)
    # print(id(l))
    print(id(l[0]))
    l.append(i)
    l.remove(i-1)


