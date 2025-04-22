a, b = input().split()

a = int(a)
b = int(b)
list1=[]
for i in range(b):
    a=list(map(float, input().split()))
    list1.append(a)
    
x =(zip(*list1))
for i in x:
    value= sum(i)/b
    print(value)