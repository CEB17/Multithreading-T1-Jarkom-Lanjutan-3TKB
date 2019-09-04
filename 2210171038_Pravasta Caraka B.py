import threading
import queue
import time
import math

# Input user untuk menentukan n deret pertama bilangan prima yang ingin dicari
value = input("Masukkan n-deret prima pertama: ")
value = int(value)

# Pembuatan array bilangan yang dibagi menjadi 3 array yang akan
# diproses pada masing-masing thread
num_list_1 = [i for i in range(0, value, 3)]
num_list_2 = [i for i in range(1, value, 3)]
num_list_3 = [i for i in range(2, value, 3)]

# Array untuk menampung hasil proses pengecekan bilangan prima
prime_list = []


def is_prime(n):
    # Jika angka n adalah 0 dan 1 maka return False
    if n in [0, 1]:
        return False

    # Akan dilakukan perhitungan untuk menentukan
    # apakah n adalah bilangan prima, dengan cara jika n dibagi
    # dengan d tidak bersisa maka return False,
    # jika bersisa maka return True
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def is_prime_handler(data):
    while True:
        # Mengambil data dari setiap queue yang terbentuk
        value = data.get()

        # Memasukkan value ke fungsi is_prime untuk dilakukan pengecekan
        result = is_prime(value)
        if result is True:
            # Jika result bernilai True maka value dimasukkan
            # ke array prime_list dengan menggunakan fungsi append()
            prime_list.append(value)

        # Mengindikasikan bahwa tugas queue telah selesai mengambil data dari queue
        # untuk dilakukan proses join()
        data.task_done()


# Membuat 3 queue
q1 = q2 = q3 = queue.Queue()

# Membuat 3 thread dan menjalankannya
thread_1 = threading.Thread(target=is_prime_handler, args=(q1,))
thread_1.start()
thread_2 = threading.Thread(target=is_prime_handler, args=(q2,))
thread_2.start()
thread_3 = threading.Thread(target=is_prime_handler, args=(q3,))
thread_3.start()

# Memproses setiap bilangan yang tersimpan
# pada array untuk dimasukkan kedalam queue
for value in num_list_1:
    q1.put(value)
for value in num_list_2:
    q2.put(value)
for value in num_list_3:
    q3.put(value)

# Untuk mencegah proses zombie
q1.join()
q2.join()
q3.join()

# Mengurutkan bilangan yang tersimpan dalam array mulai dari terkecil
prime_list.sort()

print(prime_list)
