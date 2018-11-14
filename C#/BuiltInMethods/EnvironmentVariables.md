# Environment Variables

    This method is used to find declared environment variables
    
## Code: 

    using System.IO;

    Environment.GetEnvironmentVariable("<insert environment variable>");

    
## Example

    using System.IO;
    
    namespace EnvGetVar
    {
        class Program
        {
            static void Main(string[] args)
            {
                Console.Write(Environment.GetEnvironmentVariable("ProgramFiles(x86)"));
                Console.Read();
            }
        }
    }