using System;
using System.Collections.Generic;
using System.Text;

class Methods
{
        int k, j, i, l;
        double s, s1, s2, max;


   public void SimpleIteration(int n, double [,] matrix, double [] f, double e)
    {
        for (i = 0; i < n; i++)
        {
            s = 0;
            for (j = 0; j < n; j++)
            {
                if (i != j) s = s + Math.Abs(matrix[i, j]);
            }
            if (Math.Abs(matrix[i,i])<=Math.Abs(s))
            {
                Console.WriteLine("Не задовольняє умови");
                return;
            }
        }

        double[,] x = new double[n, 2];
        l = 0; k = 0; max = 0;
        do
        {
            l++; Console.WriteLine("k=" + l);
            for (i = 0; i < n; i++)
            {
                s = 0;
                for (j = 0; j < n; j++)
                {
                    if (i != j) s = s + (matrix[i, j] / matrix[i, i]) * x[j, k];
                }

                x[i, k + 1] = f[i] / matrix[i, i] - s;
            }

            max = Math.Abs(x[1, k + 1] - x[1, k]);

            for (i = 1; i < n; i++)
            {
                if (Math.Abs(x[i, k + 1] - x[i, k]) > max) max = Math.Abs(x[i, k + 1] - x[i, k]);
            }
            Console.WriteLine("max = " + max);

            for (i = 0; i < n; i++) x[i, k] = x[i, k + 1];
            for (i = 0; i < n; i++)
            Console.WriteLine(" x[" + (i + 1) + "]=" + x[i, k]);
        }
        while (max > e);
    }


   public void Zadel_Nekrasov(int n, double [,] matrix, double [] f,  double e)
    {
        for (i = 0; i < n; i++)
        {
            s = 0;
            for (j = 0; j < n; j++)
            {
                if (i != j) s = s + Math.Abs(matrix[i, j]);
            }
            if (Math.Abs(matrix[i, i]) <= Math.Abs(s))
            {
                Console.WriteLine("Не задовольняє умови");
                return;
            }
        }

        double[,] x = new double[n, 2];
        l = 0; k = 0; max = 0;
        do
        {
            l++; Console.WriteLine("k=" + l);
            for (i = 0; i < n; i++)
            {
                s1 = 0; s2 = 0;
                for (j = 0; j < i; j++)
                {
                    s1 = s1 + (matrix[i, j] / matrix[i, i]) * x[j, k + 1];
                }
                for (j = i + 1; j < n; j++)
                {
                    s2 = s2 + (matrix[i, j] / matrix[i, i]) * x[j, k];
                }
                x[i, k + 1] = f[i] / matrix[i, i] - s1 - s2;
            }

            max = Math.Abs(x[1, k + 1] - x[1, k]);

            for (i = 1; i < n; i++)
            {
                if (Math.Abs(x[i, k + 1] - x[i, k]) > max) max = Math.Abs(x[i, k + 1] - x[i, k]);
            }
            Console.WriteLine("max = " + max);

            for (i = 0; i < n; i++) x[i, k] = x[i, k + 1];
            for (i = 0; i < n; i++)
            Console.WriteLine(" x[" + (i + 1) + "]=" + x[i, k]);
        }
        while (max > e);
    }

}

class Demonstration
{
    static void Main(string[] args)
    {
        Methods ob = new Methods();

        int n,i,j,r;
        double e;

        Console.WriteLine("Enter n");
        n = Int32.Parse(Console.ReadLine());

        double[,] x = new double[n, 2];
        double[] f = new double[n];
        double[,] matrix = new double[n, n];

        for (i = 0; i < n; i++)
        {
            for (j = 0; j < n; j++)
            {
                Console.Write("Enter a[" + (i + 1) + "," + (j + 1) + "] = ");
                matrix[i, j] = Double.Parse(Console.ReadLine());
            }
        }

        for (j = 0; j < n; j++)
        {
            Console.Write("Enter f[" + (j + 1) + "] = ");
            f[j] = Double.Parse(Console.ReadLine());
        }

        Console.WriteLine("Enter e");
        e = Double.Parse(Console.ReadLine());

        Console.WriteLine("Натисніть \n 1 (метод простої ітерації), \n 2 (метод Зейделя-Некрасова) або \n 0 (для закінчення)");

        do
            {
               r = Int32.Parse(Console.ReadLine());
               switch (r)
               {
                   case 1: ob.SimpleIteration(n, matrix, f, e); break;
                   case 2: ob.Zadel_Nekrasov(n, matrix, f, e); break;
               }

            } while (r != 0);
    }
}
