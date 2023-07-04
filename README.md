# Blog Project
Minimal blog Project built using Django. 
Django is web framework built in python programming language.
Django helps create Dynamic webpages faster as most of the basic files are  generated in the beginning by the framework.   
It has blog app and account app.
account app was built to customize user auth.

Whereas blog app to create a app essential for the project.

The Website is using Sqlite3 is database.

As SQLite is serverless as it doesn't need a different server process or system to operate. SQLite facilitates you to work on multiple databases on the same session simultaneously, thus making it flexible. 
    
    Because of the above mentioned reason a lot of time of the user is saved which would be wasted in setting up mysql sever on the linux system. My personal experience for the time being with mariadb client on linux distribution is not that favouring. Most of the time it took me hours to figure out things and install it on my laptop. Which I did by going through many online forms like stackoverflow, askubuntu, etc.


And This saves a lot of time of  user/client Who Probably writing around 2000-3000 blogs max in his/her lifetime.




<br><hr><br>

# Initial setup 

<i><h3>To create a virtual environment</h3></i>

~pip install venv <br> ~python -m venv env <br>~source env/bin/activate

<br> To deactivate:-
<br>    ~deactivate

<h2><u>Installing necessary modules:-</u></h2>


pip install -r requirements.txt


\# this is to install all the required modules for running the web applications

\# do this after getting inside the main directory of the web application



<u><h2>Applying migrations:-</u></h2>

~ python manage.py makemigrations (only if you have made any recent changes in the database.)<br>
~ python manage.py migrate<br>


<u><h2>Create Superuser:-</u></h2>

~ python manage.py createsuperuser


<u><h2>Runserver:-</u></h2>

~ python manage.py runserver
