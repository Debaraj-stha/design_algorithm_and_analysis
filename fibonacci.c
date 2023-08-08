#include<stdio.h>
int first=0;
int second=1;
void fibonacciSeries(int n){
printf("%d\t%d\t", first, second);
int i=3,next;
while(i<=n){
    next=first+second;
    first=second;
    second=next;
    printf("%d\t",next);
    i++;
}

}
int main(){
    int n;
    printf("Enter number of terms of fibonacci series:\t");
    scanf("%d",&n);
    fibonacciSeries(n);
}