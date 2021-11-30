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

    const unsigned MAX_LENGTH = 256;
    char buffer[MAX_LENGTH];
    char buffer2[MAX_LENGTH];

    for(int i = 0; fgets(buffer, MAX_LENGTH, fp); i++){
        arr[i] = atoi(buffer);
        
    }
    for(int i = 0; i <=201; i++){
        for(int j = 0; j <= 201; j++){
                for(int k = 0; k <= 201; k++){
                    if(arr[i] + arr[j] + arr[k] == 2020)
                        printf("%d * %d * %d = %d\n",arr[i], arr[j],arr[k], arr[i] * arr[j] * arr[k]);
            }
        }
    }
    fclose(fp);

    return 0;
}

