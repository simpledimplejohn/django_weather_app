# Django Weather App
A Django MVC app accessing the openweather api

## Tools
- Django
- Python3
- Decouple
- requests

## To Use This Repository
- Clone or fork this repository
- Create a .env file in the root directory
    API_KEY=''
    SECRET_KEY=''
- `python3 manage.py runservers`

# Django Wiki
Using the Django framework to create an app for the Rapid7 AP

## Setup Decouple
https://www.youtube.com/watch?v=LkyhTqDrSxA
- `pip install python-decouple`
- .gitignore
- settings.py
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', default=False, cast=bool)
    ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
- .env file
    SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    DEBUG = True
    ALLOWED_HOSTS = [localhost]
    API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
- views.py
    from decouple import config
    API_KEY = config('API_KEY')
 
## Quick Setup
1. Setup the main app
    - `django-admin startproject main .`
2. Create your app
    - `py manage.py startapp api`
3. Add the app to main
    - main/urls.py
    - add a path variable that links to the url file in your newly created app
        from django.urls import path, include
        path("", include("api.urls"))
4. Add the app to settings.py
    - INSTALLED_APPS =[,
    'api',
    ]
5. Make a page
    - create templates/api folder in api app
    - create home.html
    - create headder.html (will contain the header imported into the home page)
6. Route this page
    - api/views.py
        from . import views
        def home(response):
        return render(response, "api/home.html",{"name":"home"})
    - create api/urls.py
        - import path
        - from . import views
        - urlpatterns = []
7. Run the server
    `python3 manage.py runserver 8080` sets port
 
## External API Call
Simple Get request no key
- install requests
    - `pip install requests`
 
## VS CODE HTML SHORTCUTS
.class
#id
.class#id
!
link
a
div
ul
li
button[type=button]
 
## Setup with ENV For Windows
- Install python3 (from website)
- check python3
    - `python3 -V`
- Check pip upgrade
    - `pip install --upgrade pip`
- install virtual enviroment to pip
    - `pip install pipenv`
    - `Virtualenv location: C:\Users\john.blalock\.virtualenvs\first-vBX5j3Sl`
- create env and install Djagon in that env
    - `pipenv install django`
- Activate the enviromnemnt
    - `pipenv shell`
- Deactivate env
    - `???`
- Setup Django
    - `django-admin startproject storefront .`
 
## Running
- Test run the project
    `python3 manage.py runserver 8080` sets port
    `python manage.py runserver 0.0.0.0:8000` lets anyone see it on the local network
 
## Data Bases Django
- settings.py
    `'main.apps.MainConfig',`
- migrate
    `py manage.py migrate`
- Setup models
 
- update migration
    `py manaage.py makemigrations main`
- remigrage
    `py manage.py migrate`
 
## Use command line to CRUD objects
- Setup
    - `py manage.py shell`
    - `from main.models import Item, ToDoList`
    - `t = ToDoList(name="John List")`
    - `t.save()`
    - `ToDoList.objects.all()`
- Getbyid id
    - `ToDoList.objects.get(id=1)`
- Getbyname 
    - `ToDoList.objects.get(name="mine")`
- Create Item
- (get a ToDoList first)
    - `t.item_set.all()`
    - `t`
    - `t.item_set.create(text="stuff", complete=False)`
- Filter
    - `t.filter(name__startswith="mine")`
- Delete
    - `del_object = t.get(id=1)` # get the object
    - `del_object.delete()`
## Admin Dashboard
- `py manage.py createsuperuser`
- Add to main/admin.py
- from .models import ToDoList
 
- admin.site.register(ToDoList)