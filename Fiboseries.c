#include<stdio.h>
#include<conio.h>

void fibo(int n);

void main()
{
int n;
clrscr();
printf("\nEnter any number to find the fibonacci series \n");
scanf("%d",&n);

fibo(n);
getch();
}

void fibo(int n)
{
int i,c=0;
int a=0;
int b=1;
printf("Fibonacci series is %d:\n",n);

for(i=0;i<n;i++)
{
printf("%u  ",c);
a=b;
b=c;
c=a+b;
}
}
