using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

class Method_Giv
{
    int j, i;

    public void MultMatrixR(int n, double c, double s, int i, int j, ref double[,] a)
    {
        double[,] w = new double[n, n];
        int k;

        for (k = 0; k < n ; k++)
        {
            w[k, i] = c * a[k, i] + s * a[k, j];
            w[k, j] = c * a[k, j] - s * a[k, i];
        }
        for (k = 0; k < n; k++)
        {
            a[k, i] = w[k, i];
            a[k, j] = w[k, j];
        }

    }

    public void MultMatrixL(int n, double c, double s, int i, int j, ref double[,] a)
    {
        double[,] w = new double[n, n];
        int k;

        for (k = 0; k < n; k++)
        {
            w[i, k] = c * a[i, k] + s * a[j, k];
            w[j, k] = c * a[j, k] - s * a[i, k];
        }
        for (k = 0; k < n; k++)
        {
            a[i, k] = w[i, k];
            a[j, k] = w[j, k];
        }

    }

    public void Givens(int n, ref double[,] a)
    {
        double c, s;
        for (i = 0; i < n - 2; i++)
        {
            j = i + 2;

                do
                {
                    if (a[i, j] != 0)
                    {
                        Console.WriteLine("i= "+(i+1)+"  j="+(j+1));
                        c = a[i, i + 1] / Math.Sqrt(Math.Pow(a[i, i + 1], 2) + Math.Pow(a[i, j], 2));
                        Console.WriteLine("c = {0:f4}",c);
                        s = a[i, j] / Math.Sqrt(Math.Pow(a[i, i + 1], 2) + Math.Pow(a[i, j], 2));
                        Console.WriteLine("s = {0:f4}", s);

                        MultMatrixR(n, c, s, i+1, j, ref a);
                        MultMatrixL(n, c, s, i+1, j, ref a);
                    }
                    j++;
                }
                while (j < n);
        }
    }
}

class Demonstration
{
    static void Main(string[] args)
    {
        Method_Giv ob = new Method_Giv();

        int n, i, j;

        Console.WriteLine("Enter n");
        n = Int32.Parse(Console.ReadLine());

        double[,] matrix = new double[n, n];

        for (i = 0; i < n; i++)
        {
            for (j = i; j < n; j++)
            {
                Console.Write("Enter a[" + (i + 1) + "," + (j + 1) + "] = ");
                matrix[i, j] = Double.Parse(Console.ReadLine());
            }
        }
        for (i = 1; i < n; i++)
        {
            for (j = 0; j < i; j++) matrix[i, j] = matrix[j, i];
        }

        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n; j++)
            {
                Console.Write("{0:f2}  ", matrix[i, j]);
            }
            Console.WriteLine();
        }

        ob.Givens(n, ref matrix);

        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n; j++)
            {
                Console.Write(" {0:f5}  " , matrix[i, j]);
            }
            Console.WriteLine();
        }
    }
}