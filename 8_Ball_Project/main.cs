using System;
using System.IO;

namespace eight_Ball
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welocome to 8 Ball\nWrite your question here: ")
            string user_Input = Console.Readline();
            Random rnd = new Random();
            int eight_Ball_Rnd_Number = rnd.Next(1, 21);
            Console.WriteLine("This is a random number " + eight_Ball_Number);   
        }
    }
}
