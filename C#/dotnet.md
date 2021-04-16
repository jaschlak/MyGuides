# dotnet installs

    install packages with dotnet
    
## Microsoft.Entity FrameworkCore for SQL Server

    dotnet add package Microsoft.EntityFrameworkCore -v 5.0.1                                       ## latest stable version

    dotnet add package Microsoft.EntityFrameworkCore.tools -v 5.0.1                                 ## latest stable version

    dotnet add package Microsoft.EntityFrameworkCore.SqlServer -v 5.0.1                             ## latest stable version
	or
	dotnet add package Microsoft.EntityFrameworkCore.Sqlite -v 5.0.1								## latest stable version
	
	dotnet tool install --global dotnet-ef															## install ef db management
    
## Other Installs

    Install-Package Newtonsoft.Json                                                                 ## Newtonsoft Json Library
    
## Entity Framework

    dotnet tool install --global dotnet-ef															## install ef db management
    
    dtnet ef database update                                                                        ## create db if needed (context must be defined)
    
## Troubleshooting

    #If manifest doesn't exist, follow suggetstion and make one
    dotnet new tool-manifest