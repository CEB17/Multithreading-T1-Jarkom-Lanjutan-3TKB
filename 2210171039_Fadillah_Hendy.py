import threading
import array

angka1=int(input("Masukan batas bawah : "))
angka2=int(input("Masukan batas atas  : "))
angka3 = int(angka2*1/3)
angka4 = int(angka2*2/3)
counter = 5
arr = []

# Define a function for the thread
def bilanganprima( nomor1, nomor2):
	global counter
	if nomor1 >= 1 and nomor2 > 1:
		for x in range(nomor1,nomor2):
			prima = True
			for i in range(2,x):
				if (x%i==0):
					prima = False
			if prima == True:
				counter = counter + 1
				arr.append(x)
		
	else:
		print ("Harus bilangan bulat positif.")


# creating thread 
t1 = threading.Thread(target=bilanganprima, args=(angka1,angka3,)) 
t2 = threading.Thread(target=bilanganprima, args=(angka3,angka4,)) 
t3 = threading.Thread(target=bilanganprima, args=(angka4, angka2,)) 
  
# starting thread 
t1.start() 
t2.start() 
t3.start()
# wait until thread 1 is completely executed  
while 1:
	arr.sort()
	for i in range (0,counter):
		print (arr[i])
	break
    
    
  #Pembuatan program multithread pengurutan bilangan prima menggunakan python ini menggunakan library threading dan array, untuk code program paling atas
  #menginisialisasi angka1-angka4 sebagai inputan, kemudian counter untuk delay program dan arr(array) metode ini untuk menyimpan data agar dapat digunakan secara besamaan
  #setelah itu pada def hitung_prima adalah logika dari penghitungan bilangan prima, terjadi pengecekan angka, jika angka selain bulat positif akan sikembalikan, apabila bulat positif maka
  #akan diproses dan dicek apakah antara batas yang disebutkan tadi adakah yang termasukk bilangan prima,
  #kemdian pada thread yang pertama menjalankan fungsi bilanganprima untuk penghitungan angka1 dan angka3, kemudian thread kedua difungsi yang sama dengan penghitungan angka3 dan angka4
  #kemudian di thread ketiga dengan penghitungan angka4 dan angka2, kamudian t1,t2,t3 start hal ini yang dapat menyebabkan berjalannya thread secara bersama-sama(multithread)
  #yang terakhir adalah program untuk counter 
