# Update Live

    Update site dynamically while coding in visual studio code
    https://docs.microsoft.com/en-us/aspnet/core/mvc/views/view-compilation?view=aspnetcore-3.1&tabs=netcore-cli#runtime-compilation
    
## upon creation

    dotnet new webapp --razor-runtime-compilation
    
## existing project (edit startup.cs)

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddRazorPages()
            .AddRazorRuntimeCompilation();
    }