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

  - Remove hardcoded urls
    Using hardcoded url makes it a tightly coupled approach. Less flexible and not scalable
  

[Namespacing URLs](https://docs.djangoproject.com/en/4.1/topics/http/urls/)
-

To design URLs for an app, you create a Python module informally called a URLconf (URL configuration). This module is pure Python code and is a mapping between URL path expressions to Python functions (your views).
<br>
This mapping can be as short or as long as needed. It can reference other mappings. And, because it’s pure Python code, it can be constructed dynamically.
<br>
Django also provides a way to translate URLs according to the active language. See the internationalization documentation for more information.
<br>

  URL Namespaces
  -

  URL namespaces allow you to uniquely reverse named URL patterns even if different applications use the same URL names. It’s a good practice for third-party apps to always use namespaced URLs .Similarly, it also allows you to reverse URLs if multiple instances of an application are deployed. In other words, since multiple instances of a single application will share named URLs, namespaces provide a way to tell these named URLs apart.

  Django applications that make proper use of URL namespacing can be deployed more than once for a particular site. For example django.contrib.admin has an AdminSite class which allows you to deploy more than one instance of the admin. In a later example, we’ll discuss the idea of deploying the polls application from the tutorial in two different locations so we can serve the same functionality to two different audiences (authors and publishers).
  <br><br>
  A URL namespace comes in two parts, both of which are strings:
  <br><br>
  `application namespace`<br>
  This describes the name of the application that is being deployed. Every instance of a single application will have the same application namespace. For example, Django’s admin application has the somewhat predictable application namespace of `'admin'`.<br><br>
  instance namespace<br>
  This identifies a specific instance of an application. Instance namespaces should be unique across your entire project. However, an instance namespace can be the same as the application namespace. This is used to specify a default instance of an application. For example, the default Django admin instance has an instance namespace of `'admin'`.<br><br>
  Namespaced URLs are specified using the ':' operator. For example, the main index page of the admin application is referenced using 'admin:index'. This indicates a namespace of 'admin', and a named URL of 'index'.
  <br><br>
  Namespaces can also be nested. The named URL `'sports:polls:index'` would look for a pattern named `'index'` in the namespace `'polls'` that is itself defined within the top-level namespace `'sports'`.

[Static files](https://docs.djangoproject.com/en/4.1/howto/static-files/)
-

Websites generally need to serve additional files such as images, JavaScript, or CSS. In Django, we refer to these files as “static files”. Django provides django.contrib.staticfiles to help you manage them.


  Configuring static files
  -

  1. Make sure that django.contrib.staticfiles is included in your INSTALLED_APPS.
  2. In your settings file, define STATIC_URL, for example:

    ```py
    STATIC_URL = 'static/'
    ```
  3. In your templates, use the static template tag to build the URL for the given relative path using the configured STATICFILES_STORAGE.

    ```py
    {% load static %}
    <img src="{% static 'my_app/example.jpg' %}" alt="My image">
    ```
  4. Store your static files in a folder called static in your app. For example my_app/static/my_app/example.jpg.
    Your project will probably also have static assets that aren’t tied to a particular app. In addition to using a static/ directory inside your apps, you can define a list of directories (STATICFILES_DIRS) in your settings file where Django will also look for static files. For example:

      ```py
      STATICFILES_DIRS = [
          BASE_DIR / "static",
          '/var/www/static/',
      ]
      ```
  
  Serving static files during development
  -

  If you use django.contrib.staticfiles as explained above, runserver will do this automatically when DEBUG is set to True. If you don’t have django.contrib.staticfiles in INSTALLED_APPS, you can still manually serve static files using the django.views.static.serve() view.
<br>
  This is not suitable for production use! For some common deployment strategies, see How to deploy static files.
<br>
  For example, if your STATIC_URL is defined as static/, you can do this by adding the following snippet to your urls.py:

    ```py
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        # ... the rest of your URLconf goes here ...
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    ```

<br><br>

Read [docs](https://docs.djangoproject.com/en/4.1/howto/static-files/)....

  More about static files
  -

  - Files such as images, JS or CSS
  
The Django template language¶
-

A template contains variables, which get replaced with values when the template is evaluated, and tags, which control the logic of the template.

Below is a minimal template that illustrates a few basics. Each element will be explained later in this document.

```py
{% extends "base_generic.html" %}

{% block title %}{{ section.title }}{% endblock %}

{% block content %}
<h1>{{ section.title }}</h1>

{% for story in story_list %}
<h2>
  <a href="{{ story.get_absolute_url }}">
    {{ story.headline|upper }}
  </a>
</h2>
<p>{{ story.tease|truncatewords:"100" }}</p>
{% endfor %}
{% endblock %}

```

Adding Image Field to Model
-

- Add the following code to  `models.py` file

  ```py
  item_image =  models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRA5L8IbQ846lWwlpYLaguWNOP3mSSE0klyig&usqp=CAU")
  ```
  - Make migrations

  ```
  python manage.py makemigrations <app_name>
  ```

  ```
  python manage.py sqlmigrate <app_name migration_number>
  ```

  ```
  python manage.py migrate
  ```

- Profile image requirements
  - [`pillow`](https://pypi.org/project/Pillow/)
  
  ```
  pip install pillow
  ```