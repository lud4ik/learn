#include <stdio.h>


int nsd(int a, int b){
    int t = a > b ? a: b;
    if (a < b) {
        b = a; a = t;
    }
    while (b != 0){
        t = b; b = a % b; a = t;
    }
    return a;
}

int nsk(int a, int b){
    return (a * b) / nsd(a, b);
}


int main()
{
    int NSK, NSD, a = 4171, b = 8827;
    NSK = nsk(a, b);
    NSD = nsd(a, b);

    printf("NSK(%d, %d) = %d\n", a, b, NSK);
    printf("NSD(%d, %d) = %d\n", a, b, NSD);

    return 0;
}