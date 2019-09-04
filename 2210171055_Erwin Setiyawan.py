#menggunakan library threading dan time untuk threading dan delay
import threading
import time
#mendeklarasikan 2 threading event, untuk flag thread fibonanci_1 dan fibonanci_2
e = threading.Event()
f = threading.Event()
#deklarasi variable a,b,c untuk rumus fibonanci dan i untuk state
a=0
b=1
c=0
i=1
#menuliskan fungsi printing yang berfungsi untuk menampilkan hasil perhitungan dari fibonanci_1 dan fibonanci_2
def printing():
    #memanggil variable agar bisa digunakan dalam fungsi printing
    global a ,b , c, i
    #inti dalam loop ini adalah akan mengaktifkan thread2 selama 9 kali kemudian mengaktifkan thread3 sampai program berhenti
    #Karena pada state if i<=10 terdapat e.set yang akan ditangkap e.wait pada fibonanci_1
    #dan pada state else terdapat f.set yang akan ditangkap f.wait pada fibonanci_2
    while True:
        i = i+1
        if i <= 10 :
            e.set()
            print(a,' ', end='')
            time.sleep(1) 
        else :
            f.set()
            print(a,' ', end='')
            time.sleep(1)

#menuliskan fungsi fibonanci_1 yang berfungsi untuk mengerjakan perhitungan fibonanci
def fibonanci_1():
    global a ,b , c
    while True:
        #digunakan untuk menangkap sinyal dari e.set
        e.wait()
        #agar e.wait dapat menangkap sinyal dari e.set secara terus-menerus
        e.clear()
        c=a+b
        a=b
        b=c

#menuliskan fungsi fibonanci_2 yang berfungsi untuk mengerjakan perhitungan fibonanci        
def fibonanci_2():
    global a ,b , c
    while True:
        #digunakan untuk menangkap sinyal dari f.set
        f.wait()
        #agar f.wait dapat menangkap sinyal dari f.set secara terus-menerus
        f.clear()
        c=a+b
        a=b
        b=c

#memanggil funssi printing,fibonanci_1,dan fibonanci_2 yang dilakukan dalam thread dan dijalankan secara bersama
thread1 = threading.Thread(target = printing)
thread1.start()

thread2 = threading.Thread(target = fibonanci_1)
thread2.start()

thread3 = threading.Thread(target = fibonanci_2)
thread3.start()
