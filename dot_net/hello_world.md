# Hello World

    Get things setup in .net
    
## Download the .NET SDK

    https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install
    
## Check the install was successful

    open CMD
    type "dotnet"
    
## Make a new .Net app

    Navigate to the intended directory
    
    
    dotnet new console -o <insert app name>
    cd <app name just entered>
    
    
## Note it already houses the needed code:

using System;

namespace myApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
    
## Run your app, type the following

    dotnet run
    
## Modify the code by typing the following

    notepad Program.cs
    
## Add the date by modifying the file to the following

    Console.WriteLine("The current time is " + DateTime.Now);
    Console.WriteLine("Hello World!");
    
## Run again

    dotnet run