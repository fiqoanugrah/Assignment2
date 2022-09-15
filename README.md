# PBD Assignmen 2 Project
Muhammad Fiqo Anugrah (2106657286)

Heroku Hyperlink : https://assignment2-fiqoanugrah.herokuapp.com/katalog/

## client request to the Django web application

![assignment2fiqo](https://user-images.githubusercontent.com/87713462/190283875-14bde0a5-1496-47dc-aa7b-ff3a03da4a4c.png)

We can see the picture above illustrates from a client request to a Django-based web application and its response, first, the client will give request then it will catched by Urls.py and choose the appropriate view according to the request, right here urls.py and views.py are the controller. 
after that the view will display the template according to the request, so if it needs data from the database, views.py which is also the controller will ask the model to provide data, later then a data structure will be created based on the request in the models.py and then the model will ask again for data to the database and there are transactions between the model and the database, the model will always handle the required data in database. from the database it will be sent to the model once more then the model will respond the data to views, and after that views will choose a suitable and appropriate html template to be displayed on the webpage.

## why do we use virtual environments?

There are numerous modules and packages in Python for different uses. Installing a third-party library might be necessary for our project. The same directory is used for storage and retrieval by a different project that doesn't need any additional packages. because of this, the virtual environment can be used to create a separate isolated environment for both projects, and each project can store and retrieve packages from its own environment.

## Can we still create a django web application without virtual environment?

Yes it is, but let's suppose you want to work with two distinct Python projects, if we install all those libraries in the same default environment, then issues may occur and the default environment will become disorganized. Therefore, using a virtual environment is highly advised. It is still possible, but it is not recommended

## implement the steps from point 1 to point 4

### Step 1 (views.py)

In this first step, I added a function called show_katalog to this file that returns the render function, which has a function to display the Katalog.html

```shell
 def show_katalog(request):
   return render(request,"katalog.html", context)

data_katalog_item = CatalogItem.objects.all()
context ={
    'list_item' : data_katalog_item,
    'name': 'Muhammad Fiqo Anugrah',
    'NPM' : '2106657286'
}
```

### Step 2 (urls.py)

The views function is routed at this phase to enable the browser to display the HTML page. The show_Katalog function is called with the addition of the variable url patterns.
```shell
urlpatterns = [
   path('', show_katalog, name='show_katalog'),
]

Additionally, the URL katalog/ is registered in the urls.py file on project django using the code below.
'''
```shell
..
path('katalog/', include('katalog.urls')),
..
'''
### Step 3 (katalog.html)

Make a loop with list item on this step to take the data that is already saved inside of models.py in order to display the list of items in a table.
```shell
{% for item in list_item %}
   <tr>
     <th>{{item.item_name}}</th>
     <th>{{item.item_price}}</th>
     <th>{{item.item_stock}}</th>
     <th>{{item.rating}}</th>
     <th>{{item.description}}</th>
     <th>{{item.item_url}}</th>
   </tr>
'''
### Step 4 (Deploy)

We execute the three git commands—git add, git commit, and git push—after we've finished altering all the programs, then the repository will show all of the modified codes. Add a secret repository with the API key and the APP name to Heroku to deploy it.

