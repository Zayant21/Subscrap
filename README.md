![](Subscrap/static/images/prestored/simple%20logo.PNG)
### http://subscrap.herokuapp.com/
##### Subscription budgeting webapp made with Django framework using python , jquery and bootstrap.

## Table of contents
* [General info](#general-info)
* [Preview](#preview)
* [Technologies](#technologies)
* [Setup](#setup)


## General info
Subscrap is a web app that has its focus on allowing users to manage their subscriptions easily
while also providing knowledge on their subscription budgets. providing information on the
money being spent will help the user make smarter financial decisions in choosing which
subscriptions should be kept, and which shouldn't. The app also functions as a reminder to
avoid recurring subscriptions for services that are no longer needed .

## Preview
#### 1. Home Screen
On loading the app, the Subscrap home screen is displayed. You can go logout, go to the
home page, or search for a sample subscription.
![](Subscrap/static/images/Preview/home.PNG)

#### 2. Login
Enter Username and Password to sign in and start using the app.
![](Subscrap/static/images/Preview/login.PNG)

#### 3. Create New Account
If you are a first time user, you are required to create a username and password. This can
be done by selecting the “Sign Up” button from the login screen.
![](Subscrap/static/images/Preview/signup.PNG)

#### 4. Dashboard
After you are able to login with a valid username and password, the home screen is
displayed. The home screen is a summary of your account. There is a graph showing past
payments, a pi chart showing the distribution of types, an estimated current month
expenses, a list of all your subscriptions that can have multiple pages, and a search bar
that can search based on name and type.
![](Subscrap/static/images/Preview/mainpage.png)

#### 5. Add Subscription
To make a subscription, simply select “Add New” from the Menu.
On the add new page you will need to fill out the subscription name, cost, renewal cycle,
subscription type, url, is active, and auto renewal.
![](Subscrap/static/images/Preview/newsub.PNG)

#### 6. Edit Page
To edit a page select the pencil icon on the home page. you may choose to edit any of the
settings of the subscription chosen. Pressing submit will confirm the changes and the
return to dashboard will bring back the home page
![](Subscrap/static/images/Preview/subedit.PNG)

#### 7. Account Settings
Select the “Account Settings” button from the “Menu” on the top right corner of the screen
to view and edit settings. You can change your email and password.
![](Subscrap/static/images/Preview/accountsetting.PNG)

#### 9. Profile Settings
Select the “Profile Settings” button from the “Menu” on the top right corner of the screen
to view and edit settings. You can change your username, first name, last name,profile
pic, and write some notes.
![](Subscrap/static/images/Preview/profile_edit.PNG)
	
## Technologies
Project is created with:
* Django 3.2.9
* Python 3.8.10
* Jquery.js
* Charts.js
* bootstrap v5.0
	
## Setup
### Things we need before we start:
```
System
    Linux Environment (Windows Linux Subsystem or Any Another Linux Distro)

Coding Languages
    Python 3.8 or Above (preinstalled in Linux 18.04)

Database
    MYSQL (on Linux)

pip packages (to install run the command in Linux Terminal same directory as requirements.txt file)
  pip install -r requirements.txt
```
### Running the native build:
#### modify the settings.py file (Subscrap\Subscription\settings.py)
```
Scroll down till we see the DATABASES section, here we will insert the information about our database credentials, “username”, “password”.
```
![](Subscrap/static/images/Preview/settings.PNG)
```
Note: Before we run our app, we need to have an empty database named “Subscrap” in our Mysql.
If you are not familiar with how to create a database credentials, or a database in general go to additional help section at the bottom.
```

#### Run migrations and migrate: (\Subscrap)
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
![](Subscrap/static/images/Preview/migrate.PNG)
 
#### Run Project: (\Subscrap)
```
$ python3 manage.py runserver
```
![](Subscrap/static/images/Preview/run.PNG)

Follow the link to open the webapp page: http://127.0.0.1:8000/
