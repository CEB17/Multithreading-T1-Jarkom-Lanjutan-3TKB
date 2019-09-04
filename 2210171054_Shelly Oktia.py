import threading 

#membuat bilangan prima
def prime_1(num): 
	print("#thread 1")
	for num in range(lower,upper + 1):
	   # prime numbers are greater than 1
	   if num > 1:
       		for i in range(2,num):
           		if (num % i) == 0:
               			break
       		else:
           		print(num)


def prime_2(num): 
	print("#thread 2")
	for num in range(lower,upper + 1):
	   # prime numbers are greater than 1
	   if num > 1:
       		for i in range(1,num):
           		if (num % i) == 0:
               			break
       		else:
           		print(num)

def prime_3(num): 
	print("#thread 3")
	for num in range(lower,upper + 1):
	   # prime numbers are greater than 1
	   if num > 1:
       		for i in range(1,num):
           		if (num % i) == 0:
               			break
       		else:
           		print(num)


#main 
if __name__ == "__main__": 
	
    lower = 2 #batas bilangan prima terendah yang akan ditampilkan
    upper=input("masukan batas angka prima : ") #memasukkan input untuk menentukan batas bilangan prima tertinggi yang akan ditampilkan
    print("Prime numbers are:")

    # membuat thread 
    t1 = threading.Thread(target=prime_1, args=(10,)) 
    t2 = threading.Thread(target=prime_2, args=(10,)) 
    t3 = threading.Thread(target=prime_3, args=(10,)) 
  
    # memulai thread 1 
    t1.start() 
    # memulai thread 2 
    t2.start() 
    # memulai thread 3 
    t3.start() 
  
    # menunggu sampai thread 1 selesai dieksekusi 
    t1.join() 
    # menunggu sampai thread 2 selesai dieksekusi 
    t2.join()
    # menunggu sampai thread 3 selesai dieksekusi  
    t3.join() 
   
    print("Done!") 





