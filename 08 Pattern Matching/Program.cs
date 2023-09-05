using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SwitchCase
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 2;
            switch (a)
            {
                case 1: 
                    Console.WriteLine("Good morning");
                    break;
                case 3: { 
                        Console.WriteLine("Good day"); 
                        break; 
                    }
                case 2: 
                    Console.WriteLine("Good night");
                    break;
                default: Console.WriteLine("Default");break;
            }


        }
    }
}
