#include<stdio.h>
#include<pthread.h> //library untuk thread
#define N 30 //batas atas bilangan yag dicari prima-nya
#define NUM_THREADS 3

int prime[N]={0};//inisialisasi array bilangan
int count;

void hitung(int ptr)
{
	  int j,flag;
	  int i=ptr;
	 
	 //looping untuk mengetahui bilangan prima atau bukan
	  while(i<=N)
	    {
	        printf("Thread %d mengecek %d \n",pthread_self(),i);//checking thread sedang berlangsung
	        flag=0;//berarti bilangan prima
	        for(j=2;j<=i/2;j++)
	        {
	            if(i%j==0)
	            {
	                flag=1;//berarti bukan bilangan prima
	                break;
	            }
	        }
	
	    //jika flag bernilai 0(bilangan prima) maka boolean bernilai TRUE(1)
	    if(flag ==0 && i>1)
	     {
	       prime[i]=1;
	     }
	        i+=NUM_THREADS;
	  }

}
  
int main()
{
	    
	 pthread_t th[NUM_THREADS]={{0}};//array untuk membuat thread 
	
	//looping untuk membuat thread
	 for(count=1;count<=NUM_THREADS;count++)
	 {
	   pthread_create(&th[count],NULL,hitung,count);//berguna untuk menciptakan thread
	   pthread_join(th[count],NULL);//berguna sebagai induk thread
	 }
	
	//looping untuk print bilangan prima
	  for(count=1;count<=N;count++){
	   if(prime[count]==1)
	       printf("%d ",count);
	  }
	       
	 return 0;

 }
