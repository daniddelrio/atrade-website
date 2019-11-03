# Ateneo Trade Website

A website will be made using **Django** for Ateneo Trade.

**To set up the Django project after cloning this repo, please install MySQL on your computers and proceed to the virtualenv section of this README first before anything. For the MySQL installation, look it up on the [website](https://dev.mysql.com/)**

## Important Links
- [Google Drive Link](https://drive.google.com/open?id=1_2JE13FPKtW6TRHM6Ya4zerJDHfe8Nws)
- [Django Docs](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
- [Sample Django Project](https://github.com/yellowanthq/yellowant-sample-django-app)

## Initial Set-up

The .env file sent to you MUST BE PRESENT in the project root folder (i.e. the same folder as the manage.py). Without this .env, the website will return some errors when you try to run the server.

Whenever you run manage.py commands, remember also that your virtual environment must be activated. Read more about virtual environments below.

## Commands to Remember
### virtualenv
[Read more about python virtual environments here](https://www.geeksforgeeks.org/python-virtual-environment/)

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.

What are the commands you need to remember?
```
python -m venv ~/.virtualenvs/atrade
```
This creates a virtual environment named atrade in a folder entitled .virtualenvs. 

```
source ~/.virtualenvs/atrade/bin/activate
```
This activates your virtualenv in your Terminal window, which means you can now use the dependencies installed in your venv.

```
pip install -r requirements.txt
```
Installs all the dependencies listed in the requirements.txt of this repo to your virtualenv. Make sure your Terminal is at the same directory as the requirements.txt. **This command should be done when setting up the Django project.**

```
pip install [package_name]
```
If you find an external Python library which you think you can use for this project, you can install it in your virtualenv using this command. Don't forget to add the library and the version you installed to the requirements.txt so that other collaborators can also install the dependency in their virtualenvs.


### Github Workflow
[Very helpful interactive tutorial on the Git workflow](https://learngitbranching.js.org/)

1. Before creating a new branch from master on your local repo, make sure that you're working with the latest version of the branch. To do that, check first if you're on the master branch using ```git branch```. If you're not, you can switch to the master branch using ```git checkout master```. Then, run ```git pull```, which fetches the updated commits from the remote repo and updates your local repo accordingly.
2. Create a new branch from the master branch. You can create a branch on the remote repo (Github website) or on the local  repo (on your computer); just make sure you're branching off the master branch. To do this locally, run ```git checkout -b branch_name```.
3. Make changes to your code.
4. Run ```git status``` to see what files have been changed. To add a specific file to the stage before committing, run ```git add [path_to_file]```. To add all the changed files to the stage, run ```git add . ```.
5. After adding files to the stage, you can now commit your changes using ```git commit -m "Commit message"```.
**It is bad practice to have ALL your big changes in just one commit. Better to get used to have a purpose for each commit.** i.e. Adding only some files for a commit, then adding the other changed files for another commit, kind of like categorizing your changes.
6. Now that you've committed on your local repo, you can now push them to the remote repo using ```git push```. You can view previous commits on the branch using ```git log```.
7. After you've made all your changes on your branch, make a pull request on the Github website, attempting to merge it with the master branch.

Important commands:
```
git branch
git checkout [branch_name]
git checkout -b [new_branch]
git pull
git status
git add
git commit -m "Commit message"
git push
git log
```

### Django Commands
Please read the Django tutorials in their official docs to fully understand these commands.

```
python manage.py runserver
```
 - runs the web server (only for development)
 - to change the port: python manage.py runserver [port_number]
 - to change server’s IP: python manage.py runserver [ip]:[port]

```
python manage.py startapp [app_name]
```
 - creates an app

```
python manage.py makemigrations
```
 - adds the changes made into the database

```
python manage.py migrate
```
 - applies the changes to the database

```
python manage.py sqlmigrate [app_name] 0001
```
 - takes migration names and returns their SQL

```
python manage.py check
```
 - checks for any problems in your project without making migrations or touching the database

```
python manage.py shell
```
 - invokes the python shell
 
```
python manage.py createsuperuser
```
 - creates a user who can login to the admin site


#### In the shell:
```
from [app_name].models import [model_name]
```
 - import the model in the shell

```
[model_name].objects.all()
```
 - displays all the objects in the database

```
v = [model_name]([field_name] = [value], …)
```
 - create an object in the database

```
v.save()
```
 - saves the object into the database

```
v.id
```
 - gets the ID

```
[model_name].objects.get(pk=1)
```
 - gets the object with primary key 1

```
v.[field_name]_set.all()
```
 - displays any choices from the related object set

```
v.[field_name]_set.create(parameters…)
```
 - creates objects and adds to the related set

### MySQL
```
mysql -u root -p
```
 - opens shell of MySQL

#### In the MySQL shell:
```
DROP DATABASE atrade_db;
```
 - deletes the database named atrade_db

```
CREATE DATABASE atrade_db;
```
 - creates database named atrade_db

**Note that the username and password of your MySQL configuration, as well as the name of the database you made, must match the ones in the .env file.**
