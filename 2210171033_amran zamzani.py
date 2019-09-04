#nama : amran zamzani
#nrp  : 2210171033

#describe sourcode : pada program dibawah,melakukan 3 tread,dimana tread pertama melakukan
#                    print nilai a, kemudian tread ke 2 (fibo_1) mengeprint bilangan fibo apabila nilai  i
#                    <= val,dimana nilai val = int(nmax)/2,sedangkan tread 3 (fibo_2) mengeprint bilangan fibo
#                    apabila nilai i > val, dan akan berhenti ketika nilai i == int (nmax) sesuai nilai nmax yg diinputkan.

import threading
import time
x = threading.Event()
z = threading.Event()


a=0
b=1
c=0
i=0

nmax = input("masukan input : ")

val = int(nmax)/2
def printkondisi():
    global a ,b , c, i
    while True :
        if i <= val :
            x.set()
            #print(val)
            print(a,' ', end='')
            time.sleep(1)
            i = i+1
        else :
            z.set()
            print(a,' ', end='')
            #print("a")
            time.sleep(1)
            i = i+1
            if i == int(nmax) :
                break

def fibo_1():
    global a ,b , c
    while True:
        x.wait()
        x.clear()
        c=a+b
        a=b
        b=c
        #print nilai('a ')

def fibo_2():
    global a ,b , c
    while True:
        z.wait()
        z.clear()
        c=a+b
        a=b
        b=c
        #print nilai ('b ')


thread1 = threading.Thread(target = printkondisi)
thread1.start()

thread2 = threading.Thread(target = fibo_1)
thread2.start()

thread3 = threading.Thread(target = fibo_2)
thread3.start()

