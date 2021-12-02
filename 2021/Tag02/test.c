#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
    int j = 0;
    int *d = 0;
    int *h = 0;
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
       char ln = buffer[strlen(buffer)-2];
       // printf("%c\n", buffer[0]);
        if(buffer[0] == 'f'){
            //printf("%c %c\n", buffer[0], ln);
            h = h + ((int)ln-48);
        }
        else if(buffer[0] == 'd'){
            // printf("%c %c\n", buffer[0], ln);
             d = d + ((int)ln-48);
        }
        else if(buffer[0] == 'u'){
             //printf("%c %c\n", buffer[0], ln);
             d = d - ((int)ln-48);
        } 
    }
    printf("%d  %d\n",d,h);
}