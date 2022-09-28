
#Assignment 4

Heroku Hyperlink : 

## What does {% csrf_token %} do in the <form> element? What happens if there is no such "code snippet" in the <form> element?

'csrf_token' is useful for protecting all data from forms that use the POST method from 'breach attacks'.

if not using 'csrf_token' on '<form>', 'attacker' can easily use authenticated state of a user to send 'requests' that are not in accordance with the wishes of the user. And if the attack is successful on the admin account, it can harm the entire 'web app'

## Can we create the <form> element manually (without using a generator like {{ form.as_table }})? Explain generally how to create <form> manually.

Of course we can.
The trick is to directly create a form in HTML, starting with the `<form>` tag and ending with the `</form>` tag.

Next is to add the `method="<http-request>"` attribute to the `<form>` . tag

Then, between the two tags we can add the `<input>` tag to accept input from the user (either in the form of text or otherwise).

In the `<input>` tag, the `name="<variable-name>"` attribute must be added, so that the user input data can be retrieved by *views.py* by calling a command according to the HTTP request. For example `request.POST.get("title")` to get title input.

## Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.

1. Users provide input on existing HTML forms
2. the appropriate function in *views.py* will get input from the user in HTML using the command `request.POST.get("<name>")` and store it in a variable
3. From several existing variables (title and description), a new **Task** object will be created and will be directly saved into the database using the `<object>.save()` command
4. Then in the main function (in this case, mine is `show_todolist`), all todolists (objects **Task**) will be obtained according to their respective ownership, using the command `Task.objects.filter(user_id=request. user.id)` and send it to the HTML template as context
5. The HTML template will iterate on the *todolist* and display it as one todolist, one column in the table



## Explain how you implement the checklist above.

1.  create django app todolist with command `python manage.py startapp todolist`
2. add `path('', include('todolist.urls'))` to *urls.py* in *project_django*
3. Create **Task** class in models.py with user, date, title, and description fields
4. create registration form using UserCreationForm() in views.py. then create a function in views.py for login and logout which is integrated with the form in html with the POST method
5. implement function to create new task in main function in `show_todolist` with argument user, title, description, date by creating new object from class **Task** and save it to database
6. Create a form for creating tasks manually in the templates folder (without using forms.py) using the POST method
7. Make routing on todolist/urls.py according to requirements using the appropriate function from views.py
8. Deploy to Heroku using the Repository from GitHub. Then create 2 dummy accounts along with 3 dummy data on the website resulting from the deployment