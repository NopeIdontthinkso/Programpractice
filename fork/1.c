#include <stdio.h>
#include <unistd.h>

int main(){
    printf("durcb\n");
    int a,b,c;
    b = 0;
    a = fork();
    c = fork();
    // if (a == 0){
    //     b++;
    //     printf("%d %d %d\n",a,b,c);
    // }
    // else if (a > 0)
    // {
    //     b--;
    //     printf("%d %d %d\n",a,b,c);
    // }
    printf("jijfow%d %d\n", a,c);
}