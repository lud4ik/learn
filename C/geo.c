/* gcc geo.c -lm -o geo */
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

#define sqr(a) pow(a, 2)

typedef struct Point {
    int x;
    int y;
} Point;


float distance(Point *a, Point *b){
    return sqrt(sqr(b -> x - a -> x) + sqr(b -> y - a -> y));
}

int main()
{
    float d;
    Point *a = malloc(sizeof(Point)), *b = malloc(sizeof(Point));
    a -> x = 1; a -> y = 9;
    b -> x = 4; b -> y = 13;
    d = distance(a, b);
    printf("(%d, %d) <-> (%d, %d) = %.2f\n", a -> x, a -> y, b -> x, b -> y, d);
    free(a); free(b);

    return 0;
}