# Skripsi
Created by: Firmansyah Mukti Wijaya
Created on: 2023 03 04
# Description: Skripsi
skripsi is a simple project for my thesis in the university of PGRI Kediri. 

# How to install and run the project on your local machine
1. Clone this repository "git clone https://github.com/ikimukti/skripsi.git"
2. Create a virtual environment with python 3.11 "python -m venv env"
3. Turn on the virtual environment windows "env\Scripts\activate.bat" linux "source env/bin/activate"
4. cd to the project "cd weeai"
5. Install the django "pip install django"
6. Install the django-talwind "python -m pip install django-tailwind"
7. Install Node.js "https://nodejs.org/en/download/"
8. location npm search "where npm" if npm location is "C:\Program Files\nodejs\npm.cmd", then next step
9. cd to the project "cd weeai"
10. Install XAMPP and start the Apache and MySQL
11. Install connector MySQL "https://dev.mysql.com/downloads/installer/" and install custom > MySQL Connectors > Connector/Python
12. Install wheel "pip install wheel"
13. Install the mysqlclient "pip install mysqlclient"
14. Create a Tailwind CSS compatible Django app "python manage.py tailwind init"
15. Install Tailwind CSS dependencies "python manage.py tailwind install"
16. Start the development server by running tailwind "python manage.py tailwind start"
17. create database "weeai" in phpmyadmin
18. migrate the database "python manage.py migrate"
19. open new terminal and cd to the project "cd skripsi/weeai" and run the server "python manage.py runserver"
20. open the browser and go to "http://127.0.0.1:8000/"
21. create superuser "python manage.py createsuperuser"
    ```
    Username (leave blank to use 'ikimu'): admin
    Email address: iki.mukti@gmail.com
    Password: *********
    Password (again): *********
    Superuser created successfully.
    ```
22. open the browser and go to "http://127.0.0.1:8000/admin"
23. login with superuser "admin" and password "*********"
24. Nice, you can use the project

# How to install and use Font Awesome Free with Django
1. Open terminal and cd to the project "cd skripsi"
2. Turn on the virtual environment windows "env\Scripts\activate.bat" linux "source env/bin/activate"
3. Install Font Awesome Free "pip install --upgrade fontawesome-free"
4. Add fontawesome to INSTALLED_APPS in settings.py
    ```
    INSTALLED_APPS = [
        ...
        'fontawesome-free',
        ...
    ]
    ```
5. Collect the static files "python manage.py collectstatic"
    ```
    You have requested to collect static files at the destination
    location as specified in your settings:

        C:\Users\iki\Documents\GitHub\skripsi\weeai\static
    
    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes
    ```
6. Link the Styles you need in your base.html
    ```
    <!-- Our project just needs Font Awesome Free's Solid and Brand files -->
    <link href="{% static 'fontawesomefree/css/fontawesome.css' %}" rel="stylesheet" type="text/css">
    <link href="{% static 'fontawesomefree/css/brands.css' %}" rel="stylesheet" type="text/css">
    <link href="{% static 'fontawesomefree/css/solid.css' %}" rel="stylesheet" type="text/css">
    ```
7. Load the Font Awesome tags in your base.html
    ```
    {% load static %}
    ```
8. To use Font Awesome icons, add the following to your base.html
    ```
    <i class="fas fa-camera-retro"></i>
    ```
9. Finish 

# How to run the project on your local machine
1. Turn on the virtual environment windows "env\Scripts\activate.bat" linux "source env/bin/activate"
2. cd to the project "cd skripsi"
3. cd to the project "cd weeai"
4. Start the development server by running tailwind "python manage.py tailwind start"
5. open new terminal and cd to the project "cd skripsi/weeai" and run the server "python manage.py runserver"
6. open the browser and go to "http://127.0.0.1:8000/"
7. Nice, you can use the project

