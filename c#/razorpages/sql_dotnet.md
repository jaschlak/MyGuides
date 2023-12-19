#sql dotnet

	dotnet commands for sql
	
## prerequisites

	Install:
	Microsoft.EntityFrameworkCore
	Microsoft.EntityFrameworkCore.tools
	Microsoft.EntityFrameworkCore.<sql_variant>
    
    #ef
    dotnet tool install --global dotnet-ef
	
	Create:
	### context
	Model/<context_name>
	
		example:
		
		    public class ApplicationDbContext : DbContext
			{

				public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options)
				{
					
					// automatically add Id as an identity column
					[Key]        
					public int Id { get; set; }

					// required, name cannot be null
					[Required]
					public string Name { get; set; }

					public string Author { get; set; }
					
				}

				public DbSet<Book> Book { get; set; }

			}
			
	### if adding options instead of adding table/classes to Model context, create table classes:
	Model/<model name>
	
		example:
		
		    // Creating the book model
			public class Book
			{
				// automatically add Id as an identity column
				[Key]        public int Id { get; set; }

				// required, name cannot be null
				[Required]
				public string Name { get; set; }

				public string Author { get; set; }
			}
			
			
	### Connection string
	appsettings.json
	
		sqlite example:
		
		"ConnectionStrings": {
			"DefaultConnection": "DataSource=app.db"
		},
		
		mssql example:
		
		"ConnectionStrings": {
			"DefaultConnection": "Server=SATURN\\SQLEXPRESS;Database=booklist_db;Trusted_Connection=True;MultipleActiveResultSets=True"
		},


	### if context is empty (requires options), add context to startup
	Startup.cs
	
		example:
		
		services.AddDbContext<ApplicationDbContext>(option => option.UseSqlite(Configuration.GetConnectionString("DefaultConnection")));
		
		
## Commands

	# create migration file
	dotnet ef migrations add <migration name> --context <context class name>
	
	# send migration to sql
	dotnet ef database update --context <context class name>