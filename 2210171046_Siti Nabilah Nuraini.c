#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 3

struct thread_data
{
    int thread_id;
};

int n, count, a, j, create;

void primenumber ()
{
    for (count = 2; count < n; count++)
    {
        int isPrimary = 1;
        for (a=2; a<count; a++)
        {
            if (count%a==0)
            isPrimary = 0;
        }
    if (isPrimary == 1)
    printf ("%d\n", count);
    }
}

int main()
{
    pthread_t threads[NUM_THREADS];
    struct thread_data td[NUM_THREADS];

    printf ("Masukkan range bilangan prima yang ingin ditampilkan\n");
    scanf ("%d", &n);
    printf ("%d bilangan prima pertama adalah: \n", n);

    for (j = 0; j < NUM_THREADS; j++)
    {
        create = pthread_create (&threads[j], NULL, primenumber, (void *) &td[j]);
        pthread_join(threads[j], NULL);
        pthread_exit (NULL);
    }
return 0;
}

/*
Deskripsi :
Program di atas merupakan program untuk menampilkan bilangan prima dari range angka yang diinputkan. Pada program ini
terbagi menjadi 3 thread. Pada fungsi void primenumber didalamnya terdapat proses untuk mengecek apakah bilangan tersebut
merupakan bilangan prima dengan cara apabila angka yang diinputkan dibagi dua tidak ada sisa maka bukan bilangan prima dan jika
dibagi dua terdapat sisa maka angka akan diprint atau ditampilkan. 
*/
