#1
val = 'Python'
print(f'{val} is best')
#2 
a = [1, 2, 3]
b = a
print(a is b, end = '')
print(a==b)
#3
import random
print(random.randint(1,10))
#4
print(round(-0.5))
#5
a = ('1+3*2')
print(a)
#6
for i in range(10,15,1):
    print(i, end = ',')
#7
m = [1,2,3,4]
print(m[-2:-1])
#8
def calculate(num1,num2=4):
    res = num1*num2
    print(res)
calculate(5,6)
#9
m = 'hi'*2
print(m)
#10
mySet = {1,2,3}
mySet.pop()
print(mySet)
#11
sampleList=['Ann','Bob','Lina']
sampleList.append('Jane')
print(sampleList)
#12
for x in range(5):
    print(x, end = '')
    if x ==3:
        break
    else:
        print('hi')
#13
r = [1,1,2,3,4,5,5]
s = set(r)
t = [1,2,3,2]
print(len(s)+sum(t))
#14
list1 = []
list2 = []
list3 = list1
print(list1 == list2)
print(list1 is list2)
print(list1 is list3)
#15
def aFunc():
    var = 'aVar'
    print(var,end = '')
aFunc()
#16
def mul(x):
    return lambda y:x*y
res = mul(5)
print(res(4))
#17
for x in range(2,11,3):
    print(x, end = ',')