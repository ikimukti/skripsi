# Skripsi
Created by: Firmansyah Mukti Wijaya
Created on: 2023 03 04
# Description: Skripsi
skripsi is a simple project for my thesis in the university of PGRI Kediri. 

# How to install and run the project on your local machine
1. Clone this repository "git clone https://github.com/ikimukti/skripsi.git"
2. Create a virtual environment with python 3.11 "python -m venv env"
3. Turn on the virtual environment windows "env\Scripts\activate.bat" linux "source env/bin/activate"
4. cd to the project "cd skripsi"
5. Install the django "pip install django"
6. Install the django-talwind "python -m pip install django-tailwind"
7. Install Node.js "https://nodejs.org/en/download/"
8. location npm search "where npm" if npm location is "C:\Program Files\nodejs\npm.cmd", then next step
9. cd to the project "cd weeai"
10. Create a Tailwind CSS compatible Django app "python manage.py tailwind init"
11. Install Tailwind CSS dependencies "python manage.py tailwind install"
12. Install XAMPP and start the Apache and MySQL
13. Install connector MySQL "https://dev.mysql.com/downloads/installer/" and install custom > MySQL Connectors > Connector/Python
14. Install wheel "pip install wheel"
15. Install the mysqlclient "pip install mysqlclient"
16. Start the development server by running tailwind "python manage.py tailwind start"
17. create database "weeai" in phpmyadmin
18. migrate the database "python manage.py migrate"
19. open new terminal and cd to the project "cd skripsi/weeai" and run the server "python manage.py runserver"
20. open the browser and go to "http://127.0.0.1:8000/"
21. create superuser "python manage.py createsuperuser"
    Username (leave blank to use 'ikimu'): admin
    Email address: iki.mukti@gmail.com
    Password: **********
    Password (again): *********
    Superuser created successfully.
22. open the browser and go to "http://127.0.0.1:8000/admin"
23. login with superuser "admin" and password "*********"
