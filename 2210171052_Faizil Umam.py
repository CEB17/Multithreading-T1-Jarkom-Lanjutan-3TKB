import threading
import queue
import time
import math

#Mengelompokkan bilangan untuk dijalankan secara satu persatu
num_list_1 = [i for i in range(0, 32)]
num_list_2 = [i for i in range(33, 66)]
num_list_3 = [i for i in range(67, 100)]
prime_list = []

#Mendefinisikan bilangan prima
def is_prime(n):
    if n in [0, 1]:
        return False

    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

#Define function untuk thread
def is_prime_handler(data):
    while True:
            value = data.get()
            result = is_prime(value)
            if result is True:
                prime_list.append(value)
            data.task_done()

#q1,q2,dan q3 diproses secara berurutan dengan menggunakan fungsi Queue            
q1 = q2 = q3 = queue.Queue()
#Creating thread dan starting thread
thread_1 = threading.Thread(target=is_prime_handler, args=(q1,))
thread_1.start()
thread_2 = threading.Thread(target=is_prime_handler, args=(q2,))
thread_2.start()
thread_3 = threading.Thread(target=is_prime_handler, args=(q3,))
thread_3.start()

#Memanggil nilai yang sudah dikelompokkan
for value in num_list_1:
    q1.put(value)
#Menggunakan fungsi join, agar main proses tetap dapat berjalan
q1.join()
for value in num_list_2:
    q2.put(value)
q2.join()
for value in num_list_3:
    q3.put(value)
q3.join()

#Menampilkan hasil
print(prime_list)
