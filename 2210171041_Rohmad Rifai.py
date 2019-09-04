# Mengimport library threading
import threading
# Mendeklarasikan variabel array untuk semua angka hasil proses semua thread
fibo_all = []
# Deklarasi variable
a, b, c = 0, 0, 1
# Deklarasi inputan berupa integer
n = int(input('Sampai berapa angka yang ingin ditampilkan? '))

# Membuat fungsi fibonacci yang terdiri dari 1 parameter integer
def fibo(n):
    # global variable a, b, dan c
    global a, b, c
    # Deklarasi variable array sebagai penampung angka hasil setiap thread
    fibo_list = []
    # Looping, jika c kurang dari n akan dieksekusi
    while c < n:
        # Kondisi ini dibuat untuk menambahkan 0 ke dalam fibonacci
        if a == 0:
            # Jika a = 0, value a akan ditambahkan ke array fibo_list
            fibo_list.append(a)
            # Dan juga ditambahkan ke array fibo_all
            fibo_all.append(a)
            #Ubah value a menjadi 1 untuk menonaktifkan kondisi di atas
            a = 1
        else:
            # Mulai operasi fibonacci b = c dan c = b + c
            b, c = c, b+c
            # Menambahkan value b ke array fibo_list
            fibo_list.append(b)
            # Menambahkan value b ke array fibo_all
            fibo_all.append(b)
        # Menampilkan thread yang bekerja dan juga hasil angkanya
        print("{} = {}".format(threading.current_thread().name, fibo_list))
        # Mengeluarkan value pada array fibo_list sehingga tidak memiliki nilai
        fibo_list.pop(0)

# Membuat thread baru bernama t1
t1 = threading.Thread(target=fibo, args=(n,))
# Membuat thread baru bernama t2
t2 = threading.Thread(target=fibo, args=(n,))
# Membuat thread baru bernama t3
t3 = threading.Thread(target=fibo, args=(n,))
# Memulai thread pertama
t1.start()
# Memulai thread kedua
t2.start()
# Memulai thread ketiga
t3.start()
# Fungsi join untuk mencegah main code selesai, sehingga main code akan menunggu
# thread - thread tadi selesai
t1.join()
t2.join()
t3.join()
# Menampilkan hasil array fibo_all
print("Deret Fibonacci : {}".format(fibo_all))
