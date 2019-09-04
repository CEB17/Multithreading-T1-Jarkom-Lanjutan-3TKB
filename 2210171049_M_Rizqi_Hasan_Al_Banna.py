#M Rizqi Hasan Al Banna
#2210171049

#trading ini mengunakan konsep menunggu thrade lain untuk menjalankan trade lainnya
#dikarenakan konsep fibonanci yang berjalan berurutan dan ditentukan oleh
#2 nilai sebelumnya untuk menentukan hasil selanjutnya

#menambahkan library
import threading
import time

#digunakan untuk mengambil fungsi set and wait untuk pergantian eksekusi
#dan satu thrade 1 fungsi event()
t1_e = threading.Event()
t2_e = threading.Event()
t3_e = threading.Event()
e = threading.Event()

#variable global
c=0;
awal=0
kedua=1
a= False 

#banyak deret yang akan ditampikan
jumlah= raw_input("jumlah yang diinginkan: ");
i = int(jumlah)
deret =[None] * i

#thrade awal
def thread_awal():
	global a, c, deret,awal,kedua;
	while True:
		#fungsi if digunakan untuk ketika program pertama kali berjalan thrade ini
		#tidak perlu menunggu thrade sebelumnya yaitu thrade ke_3 
		if(a==True):
			#fungsi nya wait() adalah menunggu perintah jalan dari thrade lain
			t1_e.wait();
			hasil = awal + kedua;
			c = c+1
			deret[c]= hasil;
			print "deret[",c,"]: ",hasil;
			time.sleep(1);#memberikan delay
			awal = kedua;
			kedua = hasil;
			time.sleep(1);
			t2_e.set();# fungsi set() memerintahkan thrade lain untuk berjalan
			t1_e.clear();# fungsi clear() memerintahkan thrade ini untuk menghilangkan perintah set sebelumnya supaya fungsi wait() bisa memberhentikan program 
		else :
			a = True;
			#print "awalan"
			time.sleep(1);
			#awal=0;
			#kedua =1;
			print "deret[",c,"]: ",awal;
			time.sleep(1);
			c=c+1
			print "deret[",c,"]: ",kedua;
			time.sleep(1);
			hasil = awal + kedua;
			c = c+1
			deret[c]= hasil;
			print "deret[",c,"]: ",hasil;
			time.sleep(1);
			awal = kedua;
			kedua = hasil;
			time.sleep(1);
			t2_e.set();
			t1_e.clear();

def thread_kedua():
	global a, c, deret,awal,kedua;
	while True:
		t2_e.wait();
		#print "kedua"
		a = True;
		hasil = awal + kedua;
		c= c +1
		deret[c]= hasil;
		print "deret[",c,"]: ",hasil;
		time.sleep(1);
		awal = kedua;
		kedua = hasil;
		time.sleep(1);
		t3_e.set();
		t2_e.clear();

def thread_ketiga():
	global a, c, deret,awal,kedua;
	while True :
		t3_e.wait();
		hasil = awal + kedua;
		c= c+1
		deret[c]= hasil;
		print "deret[",c,"]: ",hasil;
		time.sleep(1);
		awal = kedua;
		kedua = hasil;
		time.sleep(1);
		t1_e.set();
		t3_e.clear();

t1 = threading.Thread(target = thread_awal)#inisialisasi 
t1.daemon = True;#ketika indukan telah memberhentikan program maka thrade akan selesai
t1.start(); #memulai thrading 

t2 = threading.Thread(target = thread_kedua)
t2.daemon = True;
t2.start();

t3 = threading.Thread(target = thread_ketiga)
t3.daemon = True;
t3.start();


try:
 	while True:
 		time.sleep(0.1)
except KeyboardInterrupt:
 	print "selesai"