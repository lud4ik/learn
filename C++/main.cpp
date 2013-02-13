#include <iostream>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <queue>
#include <stdlib.h>
#include <math.h>

using namespace std;

const int MAX_STR_SIZE = 100;
void print_array(int **array, int num);
int factorial(int num);

void exercise_1_1(){
    int num, max;
    int *a;
    cout << "Enter the array size.";
    scanf("%d", &num);
    a = new int[num];
    cout << "Enter the array items.";
    for (int i = 0; i < num; ++i ) scanf("%d", &a[i]);
    max = 0;
    for (int i = 0; i < num; ++i )
    {
        if (a[i] < 0)
        {
            if (max == 0 || a[i] > max) max = a[i];
        }
    }
    if (max == 0) cout << "There is no such elements.";
    else cout << max;
    delete [] a;
}

void exercise_1_2(){
    int num, max, min;
    int *a;
    cout << "Enter the array size.";
    scanf("%d", &num);
    a = new int[num];
    cout << "Enter the array items.";
    for (int i = 0; i < num; ++i ) scanf("%d", &a[i]);
    max = min = a[0];
    for (int i = 0; i < num; ++i )
    {
        if (a[i] < min) min = a[i];
        if (a[i] > max) max = a[i];
    }
   cout << "min=" << min << " max=" << max;
   delete [] a;
}

void exercise_1_3(){
    int num;
    float *a;
    float sum = 0, avg;
    cout << "Enter the array size.";
    scanf("%d", &num);
    a = new float[num];
    cout << "Enter the array items.";
    for (int i = 0; i < num; ++i ) scanf("%f", &a[i]);
    for (int i = 0; i < num; ++i ) sum += a[i];
    avg = sum / num;
    cout << "avg=" << avg;
    delete [] a;
}

void exercise_2_1(){
    char input[MAX_STR_SIZE], result[MAX_STR_SIZE];
    int j = 0;
    cout << "Enter text.";
    std::cin.getline(input, MAX_STR_SIZE);
    for(int i = 0; input[i]!='\0'; i++)
    {
        if (isalnum(input[i]))
        {
            result[j] = input[i];
            j++;
        }
        else
        {
            if (result[j - 1] != '\n')
            {
                result[j] = '\n';
                j++;
            }
        }
    }
    result[j] = '\0';
    cout << result;
}

void exercise_2_2(){
    char input[MAX_STR_SIZE], result[MAX_STR_SIZE];
    int j = 0, num = 0;
    cout << "Enter text.";
    std::cin.getline(input, MAX_STR_SIZE);
    for(int i = strlen(input) - 1; i >= 0; i--)
    {
        if (isalnum(input[i]))
        {
            num++;
        }
        else
        {
            if ((isalnum(input[i + 1])) && (i != 0))
            {
                for(int k = i + 1; k <= i + num; k++)
                {
                    result[j] = input[k];
                    j++;
                }
                result[j] = ' ';
                j++;
                num = 0;
            }
        }
    }
    if (isalnum(input[0]))
    {
        for(int k = 0; k <= num; k++)
            {
                result[j] = input[k];
                j++;
            }
    }
    result[j] = '\0';
    cout << result;
}

void exercise_2_3(){
    string big, small;
    int pos = -1;
    cout << "Enter the first line.";
    std::getline(cin, big, '\n');
    cout << "Enter the second line.";
    std::getline(cin, small, '\n');
    pos = big.find(small, 0);
    if (pos!=-1) cout << pos;
    else cout << "They are different.";
}

void exercise_2_4(){
    char input[MAX_STR_SIZE];
    cout << "Enter the line.";
    std::cin.getline(input, MAX_STR_SIZE);
    for(int i = 0; input[i]!='\0'; i++)
    {
        if ((i == 0 || input[i - 1] == ' ') && isalpha(input[i]))
        {
            input[i] = toupper(input[i]);
        }
    }
    cout << input;
}

void exercise_4_1(){
    int n, g = 0, way = 0, i = 0, j = 0;
    int X[] = {0, 1, 1, -1};
    int Y[] = {1, -1, 0, 1};
    enum directions {right = 0, leftdown = 1, down = 2, rightup = 3};

    cout << "Enter the array size.";
    scanf("%d", &n);

    int **array = new int*[n];
    for (int i = 0; i < n; i++) array[i] = new int[n];

    while (g < n * n)
    {
        g++;
        array[i][j] = g;
        i += X[way];
        j += Y[way];

        switch (way)
        {
            case right:
                if (i + X[leftdown] < n) way = leftdown;
                else way = rightup;
                break;
            case leftdown:
                if (!((i + X[way] < n) && (j + Y[way] >= 0)))
                {
                    if (i + X[down] < n) way = down;
                    else way = right ;
                }
                break;
            case down:
                if (j + Y[rightup] < n) way = rightup;
                else way = leftdown;
                break;
            case rightup:
                if (!((i + X[way] >= 0) && (j + Y[way] < n)))
                {
                    if (j + Y[right] < n) way = right;
                    else way = down;
                }
                break;
        }
    }
   print_array(array, n);

   for(int i = 0; i < n; i++) delete [] array[i];
   delete [] array;
}

void print_array(int **array, int num){
    for (int i = 0; i < num; i++)
    {
        for (int j = 0; j < num; j++)
        {
            printf("%3i", array[i][j]);
        }
        printf("\n");
    }

}

void exercise_4_2(){
    int n, step, way = 0, i = 0, j = 0, first = 0, num, dim, curr_dim, count;
    typedef queue<int>  Queue;
    Queue temp;
    int X[] = {0, 1, 0, -1};
    int Y[] = {1, 0, -1, 0};
    enum directions {right = 0, down = 1, left = 2, up = 3};

    cout << "Enter the array size.";
    scanf("%d", &n);

    int **array = new int*[n];
    for (int i = 0; i < n; i++) array[i] = new int[n];

    cout << "Enter the step.";
    scanf("%d", &step);

    first = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            array[i][j] = first;
            first++;
        }
    }

    print_array(array, n);
    cout << '\n';

    first = 0;

    num = (int) n / 2;
    dim = n - 2 * (num - 1);

    while (num > 0)
    {
        i = first;
        j = first;
        while (!temp.empty())  temp.pop();
        count = 1;
        curr_dim = 4 * (dim + 2 * (num - 1) - 1) + step;

        while (count <= curr_dim)
        {
            switch (way)
            {
                case right:
                    if (j == n - i - 1) way = down;
                    break;
                case down:
                    if (i == j) way = left;
                    break;
                case left:
                    if (j == n - i - 1) way = up;
                    break;
                case up:
                    if (i == j) way = right;
                    break;
            }

            temp.push(array[i][j]);
            count++;

            if (count > step + 1)
            {
                 array[i][j] = temp.front();
                 temp.pop();
            }

            i += X[way];
            j += Y[way];
        }
        num--;
        first++;
    }
   print_array(array, n);
   for(int i = 0; i < n; i++) delete [] array[i];
   delete [] array;
}

void exercise_3_1(){
    int input[3], result[3], i = 0, is_S, days_in_month;
    int days[] = {31, 28, 31, 30 ,31, 30, 31, 31, 30, 31, 30, 31};
    int daysS[] = {31, 29, 31, 30 ,31, 30, 31, 31, 30, 31, 30, 31};
    char date[11];
    char * pos;
    cout << "Enter date.";
    std::cin.getline(date, 11);
    pos = strtok (date,"/");
    while (pos != NULL)
    {
        input[i] = atoi(pos);
        i++;
        pos = strtok(NULL, "/");
    }

    if (input[0] == 31 && input[1] == 12)
    {
        result[0] = 1;
        result[1] = 1;
        result[2] = input[2] + 1;
        cout << result[0] << '/' << result[1] << '/' << result[2];
        return;
    }

    is_S = input[2] % 4;

    if (is_S == 0)   days_in_month = daysS[input[1] - 1];
    else   days_in_month = days[input[1] - 1];

    if (input[0] == days_in_month)
    {
        result[0] = 1;
        result[1] = input[1] + 1;
    }
    else
    {
        result[0] = input[0] + 1;
        result[1] = input[1];
    }
    result[2] = input[2];
    cout << result[0] << '/' << result[1] << '/' << result[2];
}

void exercise_3_2(){
    float x, e, sin, cos, item;
    int n;
    bool sign;
    cout << "Enter x.";
    scanf("%f", &x);
    cout << "Enter e.";
    scanf("%f", &e);
    item = x;
    sin = item;
    n = 3;
    sign = false;
    while (item >= e)
    {
        item = pow(x, n) / factorial(n);
        if (sign)
        {
            sin += item;
            sign = false;
        }
        else
        {
            sin -= item;
            sign = true;
        }
        n += 2;
    }
    cout << sin;

    item = 1;
    cos = item;
    n = 2;
    sign = false;
    while (item >= e)
    {
        item = pow(x, n) / factorial(n);
        if (sign)
        {
            cos += item;
            sign = false;
        }
        else
        {
            cos -= item;
            sign = true;
        }
        n += 2;
    }
    cout << cos;


}

int factorial(int num)
{
    int result = 1;
    if (num == 0 || num == 1) return 1;
    for(int i = 1; i <= num; i++) result *= i;
    return result;
}

int main()
{
    exercise_1_1();
    exercise_1_2();
    exercise_1_3();
    exercise_2_1();
    exercise_2_2();
    exercise_2_3();
    exercise_2_4();
    exercise_4_1();
    exercise_4_2();
    exercise_3_1();
    exercise_3_2();

    return 0;
}
