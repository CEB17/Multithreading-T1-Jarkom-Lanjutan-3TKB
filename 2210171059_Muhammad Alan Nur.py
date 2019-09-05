import time
import threading

//deklarasi variable
a, b, c = 0, 0, 1
//inisial input 
n = int(input('Deret angka : '))
#deklarasi variable list untuk kontainer fibonanci
fibo_all = []


def fibo(x, n):
	global a, b, c #deklarasi variable global agar dapat mengakses variable diluar function
	global fibo_all
	fibo_list = [] #variable list yang digunakan untuk melihat angka fibo dan thread yang digunakan 
	while c < n:
		if a == 0:
			fibo_list.append(a) #menambah nilai a ke dalam list fibo_list dan fibo_all
			fibo_all.append(a) 
			a = 1 #menonaktifkan kondisi (if a == 0)
		else:
			b, c = c, b+c #inisialisasi fungsi dari fibonacci 
			fibo_list.append(b) #menambahkan nilai b kedalam list fibo_list dan fibo_all
			fibo_all.append(b)
		print("{} = {}".format(threading.current_thread().name, fibo_list)) #menampilkan thread yang bekerja dan yang sedang dikerjakan
		fibo_list.pop(0) #mengapus nilai pada list 
		time.sleep(x) #berguna untuk mengurutkan thread 1-3 bekerja sama rata
		
	# print("Deret Fibo : {}".format(fibo_all))


#inisialisasi thread 1-3 
t1 = threading.Thread(target=fibo, args=(1,n,))
t2 = threading.Thread(target=fibo, args=(1,n,)) 			
t3 = threading.Thread(target=fibo, args=(1,n,)) 			

#memulai thread 1-3
t1.start()
t2.start()
t3.start()

#mencegah main program selesai sampai thread 1-3 selesai mengerjakan tugas
t1.join()
t2.join()
t3.join()
# time.sleep(n/n3)

#menampilkan semua nilai fiboanacci pada list fibo_all
print fibo_all

