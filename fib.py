def fib():
    x = 0
    y = 1
    print('x = ',x)
    while y<50:
        print('y = ', y)
        x = y
        y = x+y
fib()
print('----------------------------')
def fib1():
    x,y = 0,1
    print('x = ',x)
    while y<50:
        print('y = ', y)
        x,y = y, x+y
fib1()       

     