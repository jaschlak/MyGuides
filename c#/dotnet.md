# dotnet installs

    install packages with dotnet
    
## Microsoft.Entity FrameworkCore for SQL Server

    dotnet add package Microsoft.EntityFrameworkCore -v 5.0.1                                       ## latest stable version

    dotnet add package Microsoft.EntityFrameworkCore.tools -v 5.0.1                                 ## latest stable version

    dotnet add package Microsoft.EntityFrameworkCore.SqlServer -v 5.0.1                             ## latest stable version
	or
	dotnet add package Microsoft.EntityFrameworkCore.Sqlite -v 5.0.1								## latest stable version
	
	dotnet tool install --global dotnet-ef															## install ef db management
    
    dotnet add package Microsoft.EntityFrameworkCore.Tools --version 5.0.6                          ## add entity framework tools
    
    dotnet add package Microsoft.Extensions.Logging                                                 ## Install logging package
    
## Other Installs

    dotnet add package Newtonsoft.Json
    dotnet add package log4net --version 2.0.12
    dotnet add package Microsoft.Extensions.Configuration.CommandLine --version 5.0.0
    dotnet add package Microsoft.Extensions.Configuration.Json --version 5.0.0
    dotnet add package RestSharp --version 106.11.7

## Dotnet Create Files

    dotnet new mvc -o <app_name>                                                                    ## Create MVC
    dotnet new classlib -n <app_name>                                                               ## Create C# class
    dotnet new console -n <app_name>                                                                ## Create Console Application
    dotnet new sln -o <app_name>                                                                    ## Create a solution
    
    dotnet new --help                                                                               ## See available
    
## Build References between projects

    Navigate to the directory of the .csproj file building a reference from and run command:
    dotnet add reference <file path of reference destination .csproj>
    
## Entity Framework

    dotnet tool install --global dotnet-ef															## install ef db management
    
    dtnet ef database update                                                                        ## create db if needed (context must be defined)
    
## Initial Migration

    dotnet tool install --global dotnet-ef                                                      ## don't need unless jumped to this command
    dotnet ef migrations add <migration name>                                                   ## Creates Migration folder
    dotnet ef migrations remove                                                                 ## remove last migration
    
    dotnet ef database update                                                                   ## Update database schema
    dotnet ef database update <migration name>                                                  ## Revert database schema
    dotnet ef database drop                                                                     ## drop db
    
    dotnet ef migrations script                                                                 ## get deploy script
    dotnet ef migrations list                                                                   ## see migrations (pending if not applied to db)
    
    sqllocaldb start
    sqllocaldb stop
    sqllocaldb delete
    
## Scaffold migration from existing db

    dotnet ef dbcontext scaffold 
    Example: dotnet ef dbcontext scaffold "Server=(localdb)\mssqllocaldb;Database=Blogging;Trusted_Connection=True;" Microsoft.EntityFrameworkCore.SqlServer -o Models
    
## Troubleshooting

    #If manifest doesn't exist, follow suggetstion and make one
    dotnet new tool-manifest