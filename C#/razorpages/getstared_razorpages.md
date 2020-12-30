#Get started with razor pages

	setup Razor Pages in VS Code
	more info at https://docs.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start?view=aspnetcore-5.0&tabs=visual-studio-code
	
## Prerequisites

	install Visual Studio Code (or Visual Studio) 				https://code.visualstudio.com/Download
	C# plugin for Visual Studio Code
	.NET 5.0 SDK or later 										https://dotnet.microsoft.com/download
	
## Create initial webpage

	navigate to the location you want to save the project
	open terminal and type the following commands:
	dotnet new webapp -o <project name>
	code -r <project name>
	
## trust the cert

	dotnet dev-certs https --trust
	
## run page locally

	dotnet build
	dotnet run
	