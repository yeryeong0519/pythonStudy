a=[10,20,30]
a.append(40)
print(a)
a.append([50,60])
print(a)
b=[1,2,3,4]
b.insert(2,30)
print(b)
c=[10,20,30,40]
c[2:2]=[50,60,70]
print(c) #[10,20,50,60,70,30,40]
d=[10,20,30,40]
d[2]=[50,60,70]
print(d)
d[2]=[50,60,70]
print(d) #[10,20,[50,60,70],40]
num1=[10,20,30]
num2=[40,30]
print(num1)