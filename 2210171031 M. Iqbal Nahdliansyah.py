import queue        # queue untuk membuat stack FIFO
import threading    # import library threading

q = queue.Queue()
# fungsi membuat bilangan fibonacci
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        b, a = a, a + b
    q.put((n, a))
    return
length = int(input('Masukkan Batas : '))
for n in range(1,length,3): # melakukan looping
    # masing-masing thread menjalankan fib dengan parameter n pada fungsi fib
	t1 = threading.Thread(target=fib, args = ([n]))
	t2 = threading.Thread(target=fib, args = ([n+1]))
	t3 = threading.Thread(target=fib, args = ([n+2]))
	t1.daemon = True
	t2.daemon = True
	t3.daemon = True 	
    
	t1.start()
	t2.start()
	t3.start()
			
while not q.empty():
    n, f = q.get()
    print ("{0}".format(f)) 
