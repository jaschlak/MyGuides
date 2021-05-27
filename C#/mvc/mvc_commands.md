# MVC Commands

    Some commands for working with MVC deployment
    https://docs.microsoft.com/en-us/aspnet/core/tutorials/first-mvc-app/start-mvc?view=aspnetcore-5.0&tabs=visual-studio-code
    
## Create MVC app

    dotnet new mvc -o <app_name>
    
## Open MVC in Visual Studio Code

    code -r <app_name>
    
## trust certs

    Run program (getting untrustet cert error)
    dotnet dev-certs https --trust
    
## Install Entity Framework Libs, and logging (aspnet-codegenerator scaffolding tool)

    dotnet tool install --global dotnet-ef
    dotnet tool install --global dotnet-aspnet-codegenerator
    dotnet add package Microsoft.EntityFrameworkCore.SQLite
    dotnet add package Microsoft.AspNetCore.Diagnostics.EntityFrameworkCore
    dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Design
    dotnet add package Microsoft.EntityFrameworkCore.Design
    dotnet add package Microsoft.EntityFrameworkCore.SqlServer
    dotnet add package Microsoft.Extensions.Logging.Debug
    
## Deploy code generation

    Linux
    export PATH=$HOME/.dotnet/tools:$PATH
    
    Windows 
    
    dotnet-aspnet-codegenerator controller -name MoviesController -m Movie -dc MvcMovieContext --relativeFolderPath Controllers --useDefaultLayout --referenceScriptLibraries
    
    Parameter 	Description
    -m 	The name of the model.
    -dc 	The data context.
    -udl 	Use the default layout.
    --relativeFolderPath 	The relative output folder path to create the files.
    --useDefaultLayout 	The default layout should be used for the views.
    --referenceScriptLibraries 	Adds _ValidationScriptsPartial to Edit and Create pages.
    -sqlite 	Flag to specify if DbContext should use SQLite instead of SQL Server.
    
    dotnet aspnet-codegenerator controller -h                                                   ## get help
    
## Initial Migration

    dotnet tool install --global dotnet-ef                                                      ## don't need unless jumped to this command
    dotnet ef migrations add InitialCreate                                                      ## Creates Migration folder
    dotnet ef database update                                                                   ## Update database schema
    
    