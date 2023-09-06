#include <stdio.h>
#include<conio.h>
void swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

partition(A,p,r){
x=A[r]
i=p-1
for j=p to r-1
    if A[j]<=X 
    i=i+1;
    swap(A[i],A[j])
sweap(A[i+1],A[r])
return i+1
}
quickSort(A,p,r){
if(p<r){
    q=partition(A,p,r)
    quickSort(A,p,q-1)
    quickSort(A,q+1,r)
}
   
}
void quicksort(int arr[], int p, int r) {
    if (p < r) {
        int q = partition(arr, p, r);
        quicksort(arr, p, q - 1);
        quicksort(arr, q + 1, r);
    }
}

int main() {
    int i, n;
     printf("Quicksort");
    int arr[] = {5, 1, 33, 12, 3, 2, 73};
     
    n = sizeof(arr) / sizeof(int);
    printf("Quicksort");
    quicksort(arr, 0, n - 1);
    for (i = 0; i < n; i++) {
        printf("%d\t", arr[i]);
    }

}
