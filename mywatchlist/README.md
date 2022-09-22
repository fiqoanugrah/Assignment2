
# PBD Assignment 3 Project
Muhammad Fiqo Anugrah (2106657286)

## POSTMAN

### HTML

<img width="955" alt="image" src="https://user-images.githubusercontent.com/87713462/191658052-8decb57b-2850-4e91-85bc-5a62fb8c062d.png">

### JSON

<img width="956" alt="image" src="https://user-images.githubusercontent.com/87713462/191658202-c36d34c6-d759-49e1-83eb-b8c2016b4a9d.png">


### XML

<img width="957" alt="image" src="https://user-images.githubusercontent.com/87713462/191658264-ab817c59-3360-475d-ae4f-322655343250.png">


## The difference between JSON, XML, and HTML!

JSON stands for JavaScript Object Notation, JSON is a format used to read, store, or store information from a web server so that it can be read by users. JSON is very easy to use because it has been designed to describe itself. The data stored in JSON consists of keys and values. value can be in two structures, namely paired values ​​such as objects and values ​​in the form of primitive data types such as string, number, boolean. The JSON syntax is an instance of JavaScript Object. However, the json format is text, so creating & reading JSON can be used by other programming languages ​​such as PHP, C++, Python, and Ruby.

Then XML stands for eXtensible Markup Language. XML has been used in many web or mobile applications, which function to transmit and store data. XML has been designed to be self-descriptive, so we can understand what information we want to convey from the written data by reading the XML. This XML is just information wrapped in tags.

While HTML stands for Hypertext Markup Language or "markup language". In general, HTML is a programming standard that serves to create / build a page on a website that can later be accessed and displayed via the internet.

## why we need the data delivery when implementing on a platform!

Because we need to pass data from one stack to another in developing a platform. There are many examples of data formats that we can use to send data, but the most common are HTML, XML, and JSON.

## This is how I complete the tasks in this assignment

1. first I turn on the **virtual environment** as usual
2. Create a django-app I named it 'mywatchlist' with the 
command to start the django app:
``` shell
python manage.py startapp mywatchlist
``` 
3. Added mywatchlist app into the 'INSTALLED_APPS' variable in the 'settings.py' file inside the 'project_django' folder
4. Create a 'MyWatchList' model in the 'models.py' file in the 'mywatchlist' folder with the attributes 'watched' as a description of the film, 'title' as a film title, 'rating' as a film rating in the range 1-5, 'release_date' ie when the film was released, 'review' as a film review.
5. Run this 2 command to prepare model schema migration into Django **database** adn execute the python manage.py migrate command to apply the created model schema to the Django database.:
``` shell
python manage.py makemigrations
``` 
``` shell
python manage.py migrate
``` 
6. Create a folder named `fixtures` in the application folder that has been created namely `mywatchlist`, then create a file named `initial_mywatchlist_data.json`, then add 10 data for the `MyWatchList` object in the json file.
7. Enter the created data into **database** Django with the command `python manage.py loaddata initial_mywatchlist_data.json'.
8. Created a function that accepts a `request` parameter and returns `render(request, "mywatchlist.html")` in the `views.py` file in the `mywatchlist` folder.
9. Create a folder named `templates` in the `mywatchlist` application folder, and create a `mywatchlist.html` file in that folder.
10. Added **HTML Code** to `mywatchlist.html` file
11. Create a `urls.py` file in the `mywatchlist` folder to route the `views` function that has been created so that HTML pages can appear via **browser**. The contents of `urls.py` are:
``` shell
from django.urls import path
from mywatchlist.views import show_mywatchlist

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
]
```
12. Registering `mywatchlist` application into `urls.py` in `urlpatterns` variable in `project_django` folder with additional code:
``` shell
path('watchlist/', include('watchlist.urls')),
```
14. Import **models** in the **views** function that I created into the `views.py` file
15. Add code to `show_mywatchlist` function to call the **query** function to the **model database**, then store the results of the **query** into a variable.
16. Added `context` as the third parameter to **return** render function.
17. In `mywatchlist.html` file, do a **loop** to `list_mywatchlist` variable and call the variable name of the object that I have created.
18. Perform **Data Delievery** with XML and JSON data format as described before in Lab-2
