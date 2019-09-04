import threading #import library thread

# definisi variable array untuk menyimpan hasil
arry = [None] * 500
arry[0] = 0
arry[1] = 1
arry[2] = 1

# fungsi perhitungan bilangan fibonacci yang mereturn nilai a
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        b, a = a, a + b

    return a

# fungsi memproses dan memasukan hasi nilai perhitungan fungsi fibonacci ke dalam array
# dengan parameter start dan end dari defini thread
def process(start, end):
	for n in range(int(start),int(end+1)):
                arry[n] = fib(n)

# scan nilai dari input keyboard
val = int(input("Input : "))

# mendefini/membuat dan menjalankan 3 thread dimana target adalah fungsi process 
# dengan parameter start dan end yang di dapat dari perhitungan nilai val
# thread 1 (start = 1, end = val/3 )
# thread 2 (start = (val/3)+1, end = (val/3)*2 )
# thread 3 (start = (val/3)*2)+1, end = val )
# misalnya dengan nilai val = 12 :
# thread 1 menghitung dari 1 sampai 4
# thread 2 menghitung dari 5 sampai 8
# thread 3 menghitung dari 9 sampai 12
t1 = threading.Thread(target=process, args = ([1, int(val/3)]))
t2 = threading.Thread(target=process, args = ([int((val/3))+1, int((val/3))*2]))
t3 = threading.Thread(target=process, args = ([(int((val/3))*2)+1, val]))
t1.daemon = True
t2.daemon = True
t3.daemon = True 	
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join() 

# mencetak hasil array yang berisi nilai fibonacci dengan melakukan looping for sebanyak val
for n in range(0,val):   
    print ("{0} : {1}".format(n,arry[n])) 
