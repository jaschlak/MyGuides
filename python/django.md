# Django

    Basic Django startup info
    
## cheatsheet

    https://zappycode.com/posts/1/django-cheat-sheet

## Create and run django project (cmd)

    django-admin startproject <project name>
    cd <project name>
    python manage.py runserver
    python manage.py runserver 8080                                # set port on runtime
                
## User Control         
            
    python manage.py createsuperuser                                # create super user
    python manage.py changepassword                                 # change password
    
## create website

    python manage.py startapp <app name>
    
## add app (extension site) to installed apps list
    
    open $site_home/settings.py
    add <app name> to INSTALLED_APPS list (keep comma notation at the end)
    
## create db

    python manage.py migrate
    
## update db after installing app

    python manage.py makemigrations <appname>

    More db at:
    https://docs.djangoproject.com/en/3.2/intro/tutorial02/
    
## models for db

    add class to <app_name>/models.py                               # will require migration

    #docs
    https://docs.djangoproject.com/en/3.2/ref/models/fields/
    
## migration

    # detect and create model project for new models
    python manage.py makemigrations
    
    # apply detected and created models
    python manage.py migrate
    
## connect to mssql

    pip3 install mssql-django
    
    settings.py -> Databases:
    
        DATABASES = {
            "default": {
                "ENGINE": "mssql",
                "NAME": "<db_name>",
                "USER": "<db_username>",
                "PASSWORD": "<db_password>",
                "HOST": "<sql server hostname>\<sql instance name>",
                "PORT": "1433",
                "OPTIONS": {
                    'driver': 'ODBC Driver 17 for SQL Server' # seems to be the case even if ODBC is 13
                },
            },
        }
    
    
## create models with existing db
    
    # confirm db connection is working
    python manage.py inspectdb
    
    # push detected tables to models (note: standard django tables are added automatically, you can comment out)
    python manage.py inspectdb > models.py
    
    # make migrations and migrate
    python manage.py makemigrations
    python manage.py migrate
    
    # confirm data exists (check single column)
    <model_name>.objects.values_list('<col_name_1>', '<col_name_2>')
    
## run interactive shell for Django (add data to db)
    
    # insert into database
    python manage.py shell
    from <app_name>.models import <model_name>
    <variable name> = <model_name>(<col_name_1>=<value1>, <col_name_2>=<value2>)        # creates python object, doesn't push to db
    <variable_name>.save()                                                              # saves to db
    <model_name>.objects.all()                                                          # returns (reads) python object with entire db table
    <model_name>.objects.all()[<row_num>].<col_name_1>                                  # select cell value with column name and row number
    
    # insert without python variable instance
    python manage.py shell
    from <app_name>.models import <model_name>
    <model_name>.objects.create(<col_name_1>=<col_value>,<col_name_2>=<col_value>)
    
    # udpate data in db
    python manage.py shell
    <variable name> = <model_name>.objects.all()[<row_num>].<col_name_1>                # give row a variable name    
    <variable name>.<col_name_3> = <col_value>                                          # edit row by row variable name
    <variable_name>.save()                                                              # updates or creates db based on what already exists in db
    
    # delete data in db
    <variable name> = <model_name>.objects.all()[2]                                     # set variable as 3rd row
    <variable name>.delete()                                                            # update db with delete
    
    # add this method to a model class to return string values (this creates a more readable output for <model_name>.objects.all())
        def __str__(self):
            return "{} {}".format(self.<col_name_1>, self.<col_name_2)
            
    # read db
    <model_name>.objects.all()
    <model_name>.objects.get(<column_name>=<row_value>)                                 # note: always returns one value or errors
    <model_name>.objects.filter(<column_name>=<row_value>)                              # note: can return multiple values
    <model_name>.objects.filter(<column_name>.lte=<row_value>)                          # filter to less than or equals (using field lookups)
    
    # read specific column
    
        <model_name>.objects.values_list('<col_name_1>', '<col_name_2>')
    
        # add or functionality to searching (OR uses "|". AND uses ",")
        python manage.py shell
        from django.db.models import Q
        Book.objects.filter(Q(<column_name>.lte=<row_value> |) | Q(<column_name>=<row_value>))
        
        # chaining queries
        <variable1> = Book.objects.filter(<column_name>.lte=<row_value>)                # gets 1st filter from memory
        <variable2> = Book.objects.filter(<column_name>=<row_value>)                    # gets 2nd filter from memory
        print(variable2)                                                                # grabs filtered data from db and prints it (second execution would be cached in RAM)