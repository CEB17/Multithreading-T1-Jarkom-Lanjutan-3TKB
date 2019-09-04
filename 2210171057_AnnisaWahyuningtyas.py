import threading
from threading import Thread

a = 0
b = 1
c = 0
num = 10

def fibo():
    print("Fibonacci Thread 1 Started\n")
    global a, b, c, num
    for i in range(1,num):
        if ( i == 1 ):
            c = i
        else:
            c = a + b
            a = b
            b = c
        print(c)

def fibo2():
    print("\nFibonacci Thread 2 Started\n")
    global a, b, c, num
    for i in range(1,num):
        c = a + b
        a = b
        b = c
        print(c)        

def fibo3():
    print("\nFibonacci Thread 3 Started\n")
    global a, b, c, num
    for i in range(1,num):
        c = a + b
        a = b
        b = c
        print(c)

t1=  Thread(target=fibo)
t1.start()
t1.join()
t2=  Thread(target=fibo2)
t2.start()
t2.join()
t3=  Thread(target=fibo3)
t3.start()
t3.join()
