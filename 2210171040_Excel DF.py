#Mengimpor library threading
import threading

#Variabel array untuk menampung bilangan prima
primeNumbers = []

def main():
    #Input range angka
    val = input("List primary number from 0 to ")
    
    #Validasi input
    if(int(val) < 2):
        print("\n\nPlease input value more than 1")
        main()

    #Membuat threading
    thread1 = threading.Thread(target = primary, args=(2,1/3*int(val),"(thread 1)"))
    thread2 = threading.Thread(target = primary, args=(1/3*int(val),2/3*int(val),"(thread 2)"))
    thread3 = threading.Thread(target = primary, args=(2/3*int(val),val,"(thread 3)"))

    #Menjalankan threading
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    
    #Mencetak hasil bilangan prima
    while 1:
        if(not thread1.is_alive() and not thread2.is_alive() and not thread3.is_alive()):
            #Mengurutkan hasil
            primeNumbers.sort()
            print(primeNumbers)
            break

#Fungsi untuk mencari bilangan prima
def primary(start,val,thread):
    #Dilakukan looping sebanyak input yang diberikan
    for num in range(int(start),int(val)):
        #Boolean untuk mengecek bilangan primer
        isPrimary = True

        #Validasi bilangan primer dengan membagi input dengan n
        for x in range(2,num):
            #Jika dapat dibagi dengan selain bilangan itu sendiri, maka bukan bilangan primer
            if(num%x == 0):
                isPrimary = False
        if(isPrimary):
            print(num," ",thread)
            #Memasukkan bilangan primer ke dalam array
            primeNumbers.append(num)

main()
