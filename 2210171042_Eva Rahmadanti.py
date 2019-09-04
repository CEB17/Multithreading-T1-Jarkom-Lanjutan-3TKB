import threading
import queue
import time
import math

#Bilangan yang dibagi menjadi 3 array yang kemudian akan diproses oleh masing-masing thread
num_list_1 = [i for i in range(0, 320)]
num_list_2 = [i for i in range(330, 660)]
num_list_3 = [i for i in range(670, 1000)]
prime_list = []

#fungsi pengecekan bilangan prima atau bukan 
def is_prime(n):
    #jika n bernilai 1 atau 0 maka false
    if n in [0, 1]:  
        return False
    
    max_divisor = math.floor(math.sqrt(n)) 
    for d in range(2, 1 + max_divisor): 
        if n % d == 0:
            return False
    return True

#fungsi untuk pengambilan data
def is_prime_handler(data):
    while True:
            value = data.get() #mengambil data 
            result = is_prime(value) #mengisi var result dengan hasil dari fungsi is_prime
            if result is True: #jika result benar
                prime_list.append(value) #maka data akan dimasukkan ke array prime list dengan append
            data.task_done() #menandakan jika tugas telah selesai

q1 = q2 = q3 = queue.Queue()
#membuat 3 thread dan mengaktifkannya
thread_1 = threading.Thread(target=is_prime_handler, args=(q1,))
thread_1.start()
thread_2 = threading.Thread(target=is_prime_handler, args=(q2,))
thread_2.start()
thread_3 = threading.Thread(target=is_prime_handler, args=(q3,))
thread_3.start()

#memasukkan data array pada queue
for value in num_list_1:
    q1.put(value)
for value in num_list_2:
    q2.put(value)
for value in num_list_3:
    q3.put(value)

#untuk menunggu proses induknya selesai
q1.join()
q2.join()
q3.join()
#menampilkan hasil dari proses diatas
print(prime_list)
