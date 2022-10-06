#Assignment 4
Muhammad Fiqo Anugrah
2106657286

Heroku Hyperlink : 

[Todolist Page](https://assignment2-fiqoanugrah.herokuapp.com/todolist/)

[Register Page](https://assignment2-fiqoanugrah.herokuapp.com/todolist/register)

[Login Page](https://assignment2-fiqoanugrah.herokuapp.com/todolist/login)

[Create New Task Page](https://assignment2-fiqoanugrah.herokuapp.com/todolist/create-task)


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




# Assignment 5

## Inline vs Internal vs External CSS

Aspek | Inline | Internal | External
------|--------|----------|---------
Loction | Inside element with atrr `style` | Inside HTML with `<style>` tag  | Inside `.css` file that'll be -*import* inside tag `<tag>`
Scope | Only element that used | single page | every page that have import file

Inline CSS has the advantage of limiting to an element, but the tag will look a bit messy because of the style
mixed with HTML. Internal CSS has the advantage that it can be limited to a certain page, but if there are several
rules that are repeated for other pages, become inefficient. While external has the advantage of sharing styles to multiple pages
all at once, but to *debug* it can be a little confusing.

## Tag HTML5

`<a>` : Defines a Hyperlink <br />
`<abbr>` : Defines the abbreviated form of a longer word or phrase <br />
`<address>` : Specifies the author's contact information <br />
`<area>` : Defines a specific area in the image map <br />
`<article>` : Defines an article <br />
`<aside>` : Defines some content related to web page content <br />
`<audio>` : Insert sound or audio in HTML document <br />
`<b>` : interested in text in bold style <br />
`<base>` : Defines the base URL for all relative URLs in the document <br />
`<bdi>` : Represents text that describes the purpose of the text formatting <br />
`<bdo>` : Change the text direction <br />
`<blockquote>` : Represents a passage taken from another source <br />
`<body>` : Defines the body of a document <br />
`<br>` : has a line break <br />
`<button>` : Creates a clickable button <br />
`<canvas>` : Defines a section or region in the document <br />
`<caption>` : Defines the caption or title of a table <br />
`<cite>` : a quote or reference to another source <br />
`<code>` : Specifies text as computer code <br />
`<col>` : Defines attribute values ​​for one or more columns in the <br /> table
`<colgroup>` : Specifies attributes for multiple columns in a table <br />
`<data>` : Puts content that has a machine-readable translation <br />
`<datalist>` : Represents the predefined set of options for an input element <br />
`<dd>` : Specifies the description of dt and dl <br />
`<del>` : Represents text that has been deleted from the document <br />
`<details>` : Represents a widget where the user can get information <br />
`<dfn>` : Specifies a definition <br />
`<dialog>` : Defines a dialog box or subwindow <br />
`<div>` : Specifies a section or division in the document <br />

## Types of CSS Selector
- `*` -- Universal selector, matches all elements.
- `elementname` (example: `input`) -- Type selector, selects a tag.
- `.classname` -- Class selector, selects the tag with the class called
- `#idname` -- ID selector, selects the element that has that ID
