#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
    int j = 0;
    int arr[2001];
    char *filename = "input.txt";
    FILE *fp = fopen(filename, "r");

    if(fp == NULL)
    {
        printf("Error: could not open file %s", filename);
        return 1;
    }

    const unsigned MAX_LENGTH = 256;
    char buffer[MAX_LENGTH];
        
    for(int i = 0; fgets(buffer, MAX_LENGTH, fp); i++){
        arr[i] = atoi(buffer);
    }

    for(int i = 0; i <=2000; i++){
        if(arr[i]+arr[i+1]+arr[i+2] < arr[i+1]+arr[i+2]+arr[i+3]){
            j++;
        }
        printf("%d  %d\n",i,  j);
    }
    fclose(fp);
    
    return 0;
}
