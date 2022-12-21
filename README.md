- Start project

```
django-admin startproject <project_name>
```

- Virtual environment

```
python3 -m venv <virtual_env_name>
```

- Activate virtualenv

```
source <virtual_env_name/bin/activate>
```

- mysite directory
  - `__init__.py` - tells python tht the mysite directory is actually a python package
  - `settings.py` - contains all the settings and configuration for the django project
  - `urls.py` - contains all the url patterns which are supposed to be matched with the incoming url request

[Views and URL Patterns in Django]()
  -

  A view function, or view for short, is a Python function that takes a web request and returns a web response. This response can be the HTML contents of a web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response. This code can live anywhere you want, as long as it’s on your Python path. There’s no other requirement–no “magic,” so to speak. For the sake of putting the code somewhere, the convention is to put views in a file called views.py, placed in your project or application directory.
 - Here’s a view that returns the current date and time, as an HTML document:
```py
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```

- Create app

```
python manage.py startapp edibles
```


How Django URL Patterns Work Internally
-

[Url patters]('How+Django+url+patterns+work.pdf')

- Django -> ROUT_URLCONF -> ```py
                            ROOT_URLCONF = 'mysite.urls'
                            TEMPLATES = [ ]
                            ```
                              `settings.py`  -> `urls.py` -> Match this with incoming request -> call the view


Databases and Models
-

Large websites need large amount of data to be stored.
<br>
Data for websites is stored in a db
<br>
Data in a db is stored in form of tables/db tables
<br>
Models allow us to create db tables
<br>

Models
-

Blueprints which can be used to create db tables
<br>
Models are classes in Python
<br>
Models are created in the `models.py` file
<br>
To create a model student, simply create a class named student.

SQLite to POSTGRES
-

```sql
create user jooda; create database mysite_db role hero with password 'password';grant all priviledges on database mysite_db to jooda;alter database mysite_db owner to jooda;
```

Make migrations
-

```
python manage.py makemigrations edibles
```

- Create table

```
python manage.py sqlmigrate edibles 0001
````

- Migrate

```
python manage.py migrate
```

Storing Data in Django Database
-

|ID|item_name|item_desc|item_rice|
|--|--|--|--|
|  |  |  |  |

- Database Abstraction API- 
    - Create Object
      Create object, enter data and save
    - Update Object
    - Delete Object

Django interactive shell
-

```
python manage.py shell
```

- Add data to item table

  ```py
  from edibles.models import Item
  ```
  ```py
  # access item
  Item.objects.all()
  ```
- Create a food item
  ```py
  a = Item(item_name="Pizza", item_desc="Cheesy Pizza", item_price=20)
  ```


Django Admin Panel and Creating super user
  -

- Crete user
  ```
  python manage.py createsuperuser
  ```

`app.py`

  ````py
  from django.contrib import admin
  from .models import Item
  # Register your models here.
  admin.site.register(Item)
````

Retrieving data from database
-

  - [Queryset](https://docs.djangoproject.com/en/4.1/ref/models/querysets/)
  - [Manager](https://docs.djangoproject.com/en/4.1/topics/db/managers/)
    A Manager is the interface through which database query operations are provided to Django models. At least one Manager exists for every model in a Django application.
  - Model

Django Template Language
-

```py
{% for item in item_list %}

  <ul>
    <li>
      {{ item.id }} -- {{ item.item_name }}
    </li>
  </ul>
{% endfor %}
```

<p>
Django’s template language is designed to strike a balance between power and ease. It’s designed to feel comfortable to those used to working with HTML. If you have any exposure to other text-based template languages, such as Smarty or Jinja2, you should feel right at home with Django’s templates.
</p>

- Django Template language
- Templating engine?
  Template engines are used when you want to rapidly build web applications that are split into different components. Templates also enable fast rendering of the server-side data that needs to be passed to the application.
- Jinja2 - Templating Engine

DTL - django's default engine
-

- [Variables](https://docs.djangoproject.com/en/4.1/ref/templates/language/)

  Variables look like this: `{{ variable }}`. When the template engine encounters a variable, it evaluates that variable and replaces it with the result. Variable names consist of any combination of alphanumeric characters and the underscore ("_") but may not start with an underscore, and may not be a number. The dot (".") also appears in variable sections, although that has a special meaning, as indicated below. Importantly, you cannot have spaces or punctuation characters in variable names.

  Use a dot (.) to access attributes of a variable.

- Tags
  Tags look like this: `{% tag %}`. Tags are more complex than variables: Some create text in the output, some control flow by performing loops or logic, and some load external information into the template to be used by later variables.

  Some tags require beginning and ending tags (i.e. `{% tag %} ... tag contents ... {% endtag %})`.

  Django ships with about two dozen built-in template tags. You can read all about them in the built-in tag reference. To give you a taste of what’s available, here are some of the more commonly used tags:

  # TODO: Remove hardcoded urls
  