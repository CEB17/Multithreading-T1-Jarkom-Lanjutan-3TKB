/*Nama : Putri Milenia Fitri
NRP : 2210171044
3 Teknik Komputer B
*/

#include<stdio.h>
#include<pthread.h>

#define N 100000 // Menentukan jumlah angka prima (1-15)
#define MAX_THREADS 3 //thread dengan max sebanyak 3

int prime_arr[N]={};

void *printprime(void *ptr)
{
    int  j,flag;
    int i=(int)ptr; //i merupakan pointer ptr dengan tipe integer
    while(i<=N)
    {
        printf("Thread ke-%d, mengecek angka %d\n",pthread_self(),i); //
        flag=0;
        for(j=2;j<=i/2;j++) //untuk menghitung bilangan prima atau bukan
        {
            if(i%j==0)
            {
                flag=1;
                break;
            }
        }

        if(flag==0 && (i>1))
        {
            prime_arr[i]=1;
        }
        i+=MAX_THREADS; //melakukan pengecekan 15 angka sampai 3 thread
  }
}

int main()
{
    pthread_t tid[MAX_THREADS]={}; //fungsi data thread yang digunakan dalam deklarasi variabelyang bernama tid yang disimpan pada array MAX_THREADS
    int count=1;
    for(count=1;count<=MAX_THREADS;count++)
    {
        pthread_create(&tid[count],NULL,printprime,(void*)count); //membuat thread baru yang berjumlah 3
    }

    for(count=1;count<=MAX_THREADS;count++)
    {
        pthread_join(tid[count],NULL); //ketiga thread digabung ketika semua proses thread telah selesai atau yang telah di terminasi
    }

    printf("Bilangan Prima : ");
    for(count=1;count<=N;count++) //memproses angka berapa saja yang termasuk bilangan prima setelah dilakukan thread
        if(prime_arr[count]==1)
            printf("%d ",count);

    return 0;
 }
