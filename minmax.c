#include <stdio.h>
 int min;
 int max;

 void min_max(int arr[], int i, int j){
    int min1, max1;
    if(i == j){
        max = min = arr[i];
    }

   else if (i == j-1){
        if (arr[i] < arr[j]){
            max = arr[j];
            min = arr[i];
        }
        else{
            max = arr[i];
            min = arr[j];
        }
    }

    else{
        int mid;
        mid = (i+j)/2;
        min_max(arr, i, mid);
        max1 = max;
        min1 = min;
        min_max(arr, mid+1, j);
        if (max < max1)
            max = max1;
        if (min > min1)
            min = min1;


    }
 }


 int main(){
    int i, j;
    int arr[] = {2, 23, 45, 56,7383};
    j = sizeof(arr)/sizeof(int);
    min_max(arr, 0, j-1);
    printf("min = %d, max = %d", min, max);
 }