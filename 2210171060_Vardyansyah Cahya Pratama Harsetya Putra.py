import threading
import array as arr

prime=[]


def primary(start, inp, thread):
	for candidate in range(int(start), int(inp)):
		Primary = True
		for a in range(2, candidate):
			if(candidate%a == 0):
				Primary = False
		if(Primary):
			print(candidate, " ", thread)
			prime.append(candidate)

inp = input("Bilangan Prima dari 0 ke ")	#input bilangan

thread1 = threading.Thread(target = primary, args=(2,1/3*int(inp),"Thread 1"))	#pada multithreading tersebut menggunakan 3 parameter dimana parameter pertama sebagai mulainya dari thread pertama
thread2 = threading.Thread(target = primary, args=(1/3*int(inp),2/3*int(inp),"Thread 2"))	#parameter kedua batas penggunaan thread
thread3 = threading.Thread(target = primary, args=(2/3*int(inp),inp,"Thread 3"))			#parameter ketiga nama sebagai inisial dari thread

thread1.start()			#Memulai threading
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

while 1:
	if(not thread1.is_alive() and not thread2.is_alive() and not thread3.is_alive()):
		prime.sort()												#pada looping tersebut berfungsi sebagai sort, karena pada saat generate bilangan prima
		print(prime)												#dan ditampilkan kondisi bilangan prima akan acak. sehingga saya urutkan dengan prime.sort()
		break