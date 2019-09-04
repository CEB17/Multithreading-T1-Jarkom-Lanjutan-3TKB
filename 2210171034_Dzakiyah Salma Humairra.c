#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 3

struct thread_data //mengirim value dari input ke dalam thread
{
    int thread_id;
    char *message;
};

int n, count, c, j, rc; //mendeklarasi variabel
pthread_mutex_t lock; //mendeklarasi thread_lock

void *primenumber (void *threadarg) //fungsi thread
{
    struct thread_data *my_data;
    my_data = (struct thread_data *) threadarg;
    pthread_mutex_lock(&lock); //thread dikunci

    for (count = 2; count < n; count++) //program looping untuk cek bilangan prima atau tidak
    {
        int isPrimary = 1;
        for (c = 2; c < count; c++) //parameter untuk bilangan prima, dikarenakan yang bukan bilangan prima dapat dibagi
        {
            if (count % c == 0)
            isPrimary = 0;
        }
        if (isPrimary == 1)
        printf ("%d\n", count); //jika prima maka diprint
    }
    pthread_mutex_unlock(&lock); //thread dibuka kuncinya
}

int main()
{
    pthread_t threads[NUM_THREADS]; //memanggil fungsi thread dengan jumlah thread yang telah didefinisikan
    struct thread_data td[NUM_THREADS];

    printf ("Masukkan range angka\n");
    scanf ("%d", &n);

    printf ("bilangan prima dari range angka 1-%d \n", n);

    for (j = 2; j < NUM_THREADS; j++) //untuk menjalankan thread sesuai dengan yang sudah didefinisikan
    {
        rc = pthread_create (&threads[j], NULL, primenumber, (void *) &td[j]); //membuat thread bekerja
        pthread_join(threads[j], NULL); //memasukkan angka-angka yang diinputkan
        pthread_exit (NULL);//menghentikan thread
    }

return 0;
}
