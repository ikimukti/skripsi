# Skripsi

Created by: Firmansyah Mukti Wijaya
Created on: 2023 03 04

## About

skripsi is a simple project for my thesis in the university of PGRI Kediri.

## How to install and run the project on your local machine

1. Clone this repository "git clone <https://github.com/ikimukti/skripsi.git>"
2. Create a virtual environment with python 3.11 "python -m venv env"
3. Turn on the virtual environment windows "env\Scripts\activate.bat" linux "source env/bin/activate"
4. cd to the project "cd weeai"
5. Install the django "pip install django"
6. Install the django-talwind "python -m pip install django-tailwind"
7. Install Node.js "<https://nodejs.org/en/download/>"
8. location npm search "where npm" if npm location is "C:\Program Files\nodejs\npm.cmd", then next step
9. cd to the project "cd weeai"
10. Install XAMPP and start the Apache and MySQL
11. Install connector MySQL "<https://dev.mysql.com/downloads/installer/>" and install custom > MySQL Connectors > Connector/Python
12. Install wheel "pip install wheel"
13. Install the mysqlclient "pip install mysqlclient"
14. Install the Font Awesome Free "pip install fontawesomefree"
15. Install the Sweetify "pip install sweetify"
16. Install OpenCV "pip install opencv-python"
17. Create a Tailwind CSS compatible Django app "python manage.py tailwind init"
18. Install Tailwind CSS dependencies "python manage.py tailwind install"
19. Start the development server by running tailwind "python manage.py tailwind start"
20. create database "weeai" in phpmyadmin
21. If XAMPP account for MySQL is root and password is empty, then next step
22. migrate the database "python manage.py migrate"
23. open new terminal and cd to the project "cd skripsi/weeai" and run the server "python manage.py runserver"
24. open the browser and go to "<http://127.0.0.1:8000/>"
25. create superuser "python manage.py createsuperuser"

    ```text
    Username (leave blank to use 'ikimu'): admin
    Email address: iki.mukti@gmail.com
    Password: *********
    Password (again): *********
    Superuser created successfully.
    ```

26. Start the development server by running tailwind "python manage.py tailwind start"
27. open the browser and go to "<http://127.0.0.1:8000/admin>"
28. login with superuser "admin" and password "*********"
29. Nice, you can use the project

## How to install and use Font Awesome Free with Django

1. Open terminal and cd to the project "cd skripsi"
2. Turn on the virtual environment windows "env\Scripts\activate.bat" linux "source env/bin/activate"
3. Install Font Awesome Free "pip install --upgrade fontawesome-free"
4. Add fontawesome to INSTALLED_APPS in settings.py

    ```settings.py
    INSTALLED_APPS = [
        ...
        'fontawesome-free',
        ...
    ]
    ```

5. Collect the static files "python manage.py collectstatic"

    ```text
    You have requested to collect static files at the destination
    location as specified in your settings:

        C:\Users\iki\Documents\GitHub\skripsi\weeai\static
    
    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes
    ```

6. Link the Styles you need in your base.html

    ```html
    <!-- Our project just needs Font Awesome Free's Solid and Brand files -->
    <link href="{% static 'fontawesomefree/css/fontawesome.css' %}" rel="stylesheet" type="text/css">
    <link href="{% static 'fontawesomefree/css/brands.css' %}" rel="stylesheet" type="text/css">
    <link href="{% static 'fontawesomefree/css/solid.css' %}" rel="stylesheet" type="text/css">
    ```

7. Load the Font Awesome tags in your base.html

    ```text
    {% load static %}
    ```

8. To use Font Awesome icons, add the following to your base.html

    ```html
    <i class="fas fa-camera-retro"></i>
    ```

9. Finish

## How to run the project on your local machine

1. Turn on the virtual environment windows "env\Scripts\activate.bat" linux "source env/bin/activate"
2. cd to the project "cd skripsi"
3. cd to the project "cd weeai"
4. Start the development server by running tailwind "python manage.py tailwind start"
5. open new terminal and cd to the project "cd skripsi/weeai" and run the server "python manage.py runserver"
6. open the browser and go to "<http://127.0.0.1:8000/>"
7. Nice, you can use the project

## Python Environment packages list (pip freeze) & Visual Studio Code Extensions

1. pip freeze

    ```python
    arrow==1.2.3
    asgiref==3.6.0
    binaryornot==0.4.4
    certifi==2022.12.7
    chardet==5.1.0
    charset-normalizer==3.1.0
    click==8.1.3
    colorama==0.4.6
    cookiecutter==2.1.1
    Django==4.2
    django-browser-reload==1.7.0
    django-tailwind==3.5.0
    fontawesomefree==6.4.0
    idna==3.4
    Jinja2==3.1.2
    jinja2-time==0.2.0
    MarkupSafe==2.1.2
    mysqlclient==2.1.1
    numpy==1.24.2
    opencv-python==4.7.0.72
    python-dateutil==2.8.2
    python-slugify==8.0.1
    PyYAML==6.0
    requests==2.28.2
    six==1.16.0
    sqlparse==0.4.3
    sweetify==2.3.1
    text-unidecode==1.3
    tzdata==2023.3
    urllib3==1.26.15
    ```

2. Visual Studio Code Extensions

    ```text
    1. Auto Rename Tag (Jun Han) link: https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag
    2. Code GPT (Code GPT) link: https://marketplace.visualstudio.com/items?itemName=OpenAI.codex
    3. CSS Formatter (Martin Aeschlimann) link: https://marketplace.visualstudio.com/items?itemName=aeschli.vscode-css-formatter
    4. CSS Peek (Pranay Prakash) link: https://marketplace.visualstudio.com/items?itemName=pranaygp.vscode-css-peek
    5. Djaneiro - Django Snippets (Scott Barkman) link: https://marketplace.visualstudio.com/items?itemName=ScottBarkman.djaneiro
    6. Django (Baptiste Darthenay) link: https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django
    7. Django (Roberth Solis) link: https://marketplace.visualstudio.com/items?itemName=roberthsolis.vscode-django
    8. Django Commands (MaxChamps) link: https://marketplace.visualstudio.com/items?itemName=MaxChamps.vscode-django-commands
    9. Django Snippets (bibhasdn) link: https://marketplace.visualstudio.com/items?itemName=bibhasdn.django-snippets
    10. Django Snippets (Siddharth Singha Roy) link: https://marketplace.visualstudio.com/items?itemName=siddharthroy12.django-snippets
    11. Django Template (bibhasdn) link: https://marketplace.visualstudio.com/items?itemName=bibhasdn.django-html
    12. django-intellisense (shamanu4) link: https://marketplace.visualstudio.com/items?itemName=shamanu4.django-intellisense
    13. DotENV (mikestead) link: https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv
    14. EditorConfig for VS Code (EditorConfig) link: https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig
    15. Electron Color Theme (Kus Camara) link: https://marketplace.visualstudio.com/items?itemName=kuscamara.electron
    16. ESLint (Microsoft) link: https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint
    17. Git Graph (mhutchie) link: https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph
    18. Git History (Don Jayamanne) link: https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory
    19. GitHub Pull Requests and Issues (GitHub) link: https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github
    20. GitLens — Git supercharged (GitKraken) link: https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens
    21. HTML CSS Support (ecmel) link: https://marketplace.visualstudio.com/items?itemName=ecmel.vscode-html-css
    22. HTML Snippets (Mohamed Abusaid) link: https://marketplace.visualstudio.com/items?itemName=abusaidm.html-snippets
    23. HTML Snippets (geyao) link: https://marketplace.visualstudio.com/items?itemName=geyao.html-snippets
    24. indent-rainbow (oderwat) link: https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow
    25. IntelliSense for CSS class names in HTML (Zignd) link: https://marketplace.visualstudio.com/items?itemName=Zignd.html-css-class-completion
    27. isort (Microsoft) link: https://marketplace.visualstudio.com/items?itemName=ms-python.isort
    28. Live Preview (Microsoft) link: https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server
    29. npm (Microsoft) link: https://marketplace.visualstudio.com/items?itemName=eg2.vscode-npm-script
    30. npm Intellisense (Christian Kohler) link: https://marketplace.visualstudio.com/items?itemName=christian-kohler.npm-intellisense
    31. PostCSS Language Support (csstools) link: https://marketplace.visualstudio.com/items?itemName=csstools.postcss
    32. Pylance (Microsoft) link: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
    33. Python (Microsoft) link: https://marketplace.visualstudio.com/items?itemName=ms-python.python
    34. SQLTools (Matheus Teixeira) link: https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools
    35. Tailwind CSS IntelliSense (Tailwind Labs) link: https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss
    36. Tailwind Shades (Omar Bourhaouta) link: https://marketplace.visualstudio.com/items?itemName=omar-bouh.tailwindshades
    37. Beautify (HookyQR) link: https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify
    38. GitHub Copilot (GitHub) link: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot
    39. Prettier - Code formatter (Prettier) link: https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode
    40. Nightly GitHub Copilot (GitHub) link: https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-nightly
    ```
