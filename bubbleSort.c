#include<stdio.h>
void swap(int *a, int *b){
    int temp;
    temp=*a;
   *a=*b;
   *b=temp;
}
void bubbleSort(int arr[],int n){
   int i,j;
   for(i=0;i<n-1;i++){
    for(j=0;j<n-i-1;j++){
        if(arr[j]>arr[j+1])
        swap(&arr[j],&arr[j+1]);
    }
   }
}
int main(){
int i,n;
    int arr[]={6,2,9,3,22,32};
    n=sizeof(arr)/sizeof(int);
    bubbleSort(arr,n);
    for(i=0;i<n;i++){
        printf("%d\t",arr[i]);
    }
}