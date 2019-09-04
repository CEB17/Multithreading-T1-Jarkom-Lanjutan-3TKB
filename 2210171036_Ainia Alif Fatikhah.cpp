#include <iostream>
#include <thread>
//#include <pthread.h>

using namespace std;

//#define NUM_THREADS 3
int batas,a,b,mod;      //integer untuk deklarasi tipe data yang dipakai
void thread_function()  //program dari bilangan prima
{
    for (a=2;a<=batas;a++){ 
        mod=1;
        for (b=2;b<a;b++){
            if(a%b==0){
                mod=0;
                
            }
        }
        if(mod==1){
            cout<<a<<" ";
            
        }
        ::cout<<"Thread = "<<this_thread::get_id()<<std::endl; ///digunakanuntuk memberikan id secara acak
    }
       
}


int main()  
{
    cout<<"Masukkan Batas Nilai Bilangan Prima = ";cin>>batas; //perintah untuk menginputkan nilai dari bilangan prima
    cout<<"------------------------------------------- \n";
    std::thread threadObj1(thread_function); // thread yang digunakan untuk memanggil fungsi void thread_function
    std::thread threadObj2(thread_function);
    std::thread threadObj3(thread_function);
    
 
    //if(threadObj1.get_id() != threadObj2.get_id())
    //    std::cout<<"From Main Thread :: ID of Thread 1 = "<<threadObj1.get_id()<<std::endl;    //get_id() digunakan untuk menampilkan id secara acak
    //    std::cout<<"From Main Thread :: ID of Thread 2 = "<<threadObj2.get_id()<<std::endl;    

 
    threadObj1.join();    // digunakan untuk memanggil threadObj1,threadObj2,threadObj3,
    threadObj2.join();      
    threadObj3.join();  // fungsi join() itu sendiri se penangkapan yang saya yang sudah dijelaskan tadi yaitu
    //digunakan untuk memberhentikan proses yang ada pada program yang kemudian induk nya akan berhenti (thread akan berhenti setelah program bilangan prima selesai diproses). 
    return 0;
}
