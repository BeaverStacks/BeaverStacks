# Beaver Budgets
Personal budgeting application 


<!-- ABOUT THE PROJECT -->
## About Beaver Budgets

<!-- ![{example use gif}][example-use] -->

BeaverBudgets is a personal finance web app which allows the user to create a categorized budget and enter day-to-day transactions to track spending. The app provides useful information to facilitate financial decision making for the user, including a snapshot of the remaining budget and total expenditures for each category, as well as data visualizations to summarize spending.

<!-- **Note: Beaver Budgets only supports the Windows platform at the moment.** -->


<!-- ### Built With -->

* [Django](https://www.djangoproject.com/): a Python web application framework


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

In order to use Beaver Budgets, you must first have Python and pip installed on your system. If you need assistance installing these prerequisites, see the folowing steps:
* Python is a programming language. All of this project's code base is written in Python. Download the latest version of [Python](https://www.python.org/downloads/) and install onto your local machine.

* Pip is the package installer for Python. Once Python is installed, open your local machine's command line and use the following command to utilize Python to install Pip:
```sh
python get-pip.py -g
```

Git is a version control system. In this project, Git is used to clone (copy) the most up-to-date project files from GitHub to your local machine. Download the latest version of [git](https://git-scm.com/download/win) and install on your local machine.


### One-Time Installation Process

1. Open the command line on your local machine, or a terminal from within your IDE of choice.

2. Enter the following command to use Git to clone this repository to your local machine.
```sh
git clone https://github.com/BeaverStacks/BeaverStacks.git
```
3. Enter the following command to create a new virtual environment to install this repository's dependencies.
```sh
virtualenv env
```
4. Enter the following command to activate the virtual environment you have just set up. This should shove a little (env) to the left of your command line to show it's working.
```sh
env\scripts\activate.bat
```
5. Enter the following command to upgrade Pip to to the latest version.
```sh
python.exe -m pip install --upgrade pip
```
6. Enter the following command to use Pip to install this repository's dependencies.
```sh
pip install -r requirements.txt
```
7. Enter the following command to install bower, which will handle the javascript installation stuff needed to run the neato-stuff behind the HTML.
```sh
npm install bower
```
8. Now we need to make some changes to the `\env\Lib\site-packages\django\conf\global_settings.py` file created within your virtual environment.
Just open up the above settings file in your IDE and make the following three changes:

1) Add the following to the top of global_settings.py:
```py
import os   
from pathlib import Path    
# source: https://docs.djangoproject.com/en/3.1/howto/overriding-templates/ 
# attempting to override templates using this   
BASE_DIR = Path(__file__).resolve().parent.parent
```

2) Replace line 216 of global_settings.py `TEMPLATES = []` with:
```py
    # I don't know if this works but doing this based on this: https://youtrack.jetbrains.com/issue/PY-39296    
TEMPLATES = [   
    {   
        "BACKEND": "django.template.backends.jinja2.Jinja2",    
        "DIRS": [os.path.join(BASE_DIR, "templates")],  
        "APP_DIRS": True,   
    },  
    {   
        "BACKEND": "django.template.backends.django.DjangoTemplates",   
        "DIRS": [os.path.join(BASE_DIR, "templates")],  
        "APP_DIRS": True,   
        "OPTIONS": {    
            "context_processors": [ 
                "django.template.context_processors.debug", 
                "django.template.context_processors.request",   
                "django.contrib.auth.context_processors.auth",  
                "django.contrib.messages.context_processors.messages",  
            ],  
        },  
    },  
]
```

3) Replace line 455 of global_settings.py `MIDDLEWARE = []` with:
```py
# MIDDLEWARE = [    
# 'django.contrib.messages.middleware.MessageMiddleware',   
# 'django.contrib.sessions.middleware.SessionMiddleware',   
# 'django.contrib.auth.middleware.AuthenticationMiddleware']    
# Added these because I was getting middleware errors IDK what these do lol  -AH    
# received this error:  
# ?: (admin.E409) 'django.contrib.messages.middleware.MessageMiddleware' must be in MIDDLEWARE in order to use the admin application.   
# https://docs.djangoproject.com/en/3.1/topics/http/middleware/#:~:text=Middleware%20order%20and%20layering,the%20core%20of%20the%20onion.  
# attempting this to get things going   
MIDDLEWARE = [  
    'django.middleware.security.SecurityMiddleware',    
    'django.contrib.sessions.middleware.SessionMiddleware', 
    'django.middleware.common.CommonMiddleware',    
    'django.middleware.csrf.CsrfViewMiddleware',    
    'django.contrib.auth.middleware.AuthenticationMiddleware',  
    'django.contrib.messages.middleware.MessageMiddleware', 
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   
]  
``` 


9. Pop back into your command line and change directories into the 'hackathon_starter' folder.
```sh
cd hackathon_starter
```
10. Run the final migration to connect all the broken pieced of Django with our updated global_settings.py file:
```sh
python manage.py migrate
```
11. And finally, we can run our local server:
```sh
python manage.py runserver
```

Woohoo! Now you can open up `http://localhost:8000/` in your browser to see the website in all its glory. Live it! Breathe it! <em>Welcome to Beaver Budgets!</em>




<!-- USAGE EXAMPLES -->
## Usage

One you have all the parts installed, you should theoretically be able to open everything back up without so many steps. You should be able to run the following four commands to get back up and running:
```sh
virtualenv env
env\scripts\activate.bat
cd hackathon_starter
python manage.py runserver
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/asa-leholland/{repo-name}/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Open Source Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- CONTACT -->
## Contact Beaver Stacks

Charlie Magill
Kenneth Street
Jacob Ogle
Asa LeHolland: asaleholland@gmail.com



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew](https://github.com/othneildrew) for creating the [template README file](https://github.com/othneildrew/Best-README-Template) that was used as the starting point for the README for this project. 

* [All the cool people over at Django Hackathon Starter](https://github.com/DrkSephy/django-hackathon-starter) for creating the base Django skeleton that was used as the overall starting point for this project. 






<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-url]: https://www.linkedin.com/in/asa-holland-a2a0b5b7/
[example-use]: images/{filename}.gif





<!-- LICENSE -->
## License

The MIT License (MIT)

Copyright (c) 2015 David Leonard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
