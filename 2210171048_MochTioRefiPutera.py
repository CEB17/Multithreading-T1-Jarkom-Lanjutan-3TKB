import threading
import queue
import time
import math

#Bilangan dikelompokkan terlebih dahulu agar proses threadingnya lebih mudah
list_1 = [i for i in range(0, 32)]
list_2 = [i for i in range(33, 66)]
list_3 = [i for i in range(67, 100)]
prime_list = []

#mendefinisikan rumus bilangan prima
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

#mendefiniskan fungsi untuk dimasukkan kedalam thread
def is_prime_handler(data):
    while True:
            value = data.get()
            result = is_prime(value)
            if result is True:
                prime_list.append(value)
            data.task_done()

#Menggunakan fungsi queue agar q1,q2 dan q3 diproses secara berurutan
q1 = q2 = q3 = queue.Queue()

#membuat thread
t1 = threading.Thread(target=is_prime_handler, args=(q1,))
t2 = threading.Thread(target=is_prime_handler, args=(q2,))
t3 = threading.Thread(target=is_prime_handler, args=(q3,))

#Kemudian thread tersebut dijalankan
t1.start()
t2.start()
t3.start()

#Bilangan yang dikelompokkan diawal tadi diproses satu persatu
for value in list_1:
    q1.put(value)
#Menggunakan fungsi join agar main proses tetap berjalan
q1.join()
for value in list_2:
    q2.put(value)
q2.join()
for value in list_3:
    q3.put(value)
q3.join()

#menampilkan hasil
print(prime_list)
