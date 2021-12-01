#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
    
    int arr[201];
    char *filename = "input.txt";
    FILE *fp = fopen(filename, "r");

    if(fp == NULL)
    {
        printf("Error: could not open file %s", filename);
        return 1;
    }

fclose(fp);

return 0;
}