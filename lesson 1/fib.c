//fib.c


#include <stdio.h>
int fib(int);
int main(int argc, const char * argv[]) {
    int n=10;
    //calls the function 10 times
    for(int i=0;i<=n;i++){
        int f = fib(i);
        printf("%d\n", f);
    }
    return 0;
}
//calculates the fibonacci seq using an array
int fib(int n){
    static int f[200];
    f[0] = 0;
    f[1] = 1;
    for(int i=2; i <= n;i++){
        f[i] = f[i-1] + f[i-2];
    }
    return f[n];
}
