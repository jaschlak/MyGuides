# Django

    Basic Django startup info
    
## cheatsheet

    https://zappycode.com/posts/1/django-cheat-sheet

## Create and run django project (cmd)

    django-admin startproject <project name>
    cd <project name>
    python3 manage.py runserver
    python3 manage.py runserver 8080                                # set port on runtime
                
## User Control         
            
    python manage.py createsuperuser                                # create super user
    python manage.py changepassword                                 # change password
    
## create website

    python3 manage.py startapp <app name>
    
## add app (extension site) to installed apps list
    
    open $site_home/settings.py
    add <app name> to INSTALLED_APPS list (keep comma notation at the end)
    
## create db

    python3 manage.py migrate
    
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
    python3 manage.py makemigrations
    
    # apply detected and created models
    python3 manage.py migrate