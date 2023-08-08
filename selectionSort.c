#include <stdio.h>
void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
void selectionSort(int arr[], int n)
{
    int least, p, i, j;
    for (i = 0; i < n; i++)
    {
        least = arr[i];
        p = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < least)
            { // Compare with 'least' instead of 'arr[i]'
                least = arr[j];
                p = j;
            }
            
        }

        swap(&arr[i], &arr[p]);
        int k=0;
            for (k=0; k < n; k++)
            {
                printf("%d\t", arr[k]);
            }
            printf("\n");
    }
}

int main()
{
    int i, n;
    int arr[] = {6, 2, 9, 3, 100, 32};
    n = sizeof(arr) / sizeof(int);
    selectionSort(arr, n);
    for (i = 0; i < n; i++)
    {
        printf("%d\t", arr[i]);
    }
}