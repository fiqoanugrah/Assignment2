## Asynchronus Programming and Synchronus programming
- Asynchronic programming: multi-thread which means that operations or programs can run in parallel, non-blocking which means that it can send multiple requests to the server
- Synchronus programming: single-thread which means it can only run one operation or program at a time, blocking which means it can only send one request to the server and can send another request if the previous request has been completed

## Event-Driven Programming Paradigm
- a paradigm in which entities communicate indirectly by sending messages to other entities through an intermediary.
- example: when the `Add Task` button is clicked by the user, it will cause an event to occur, namely a modal will appear on the website page

## Asynchronic Programming on AJAX
AJAX is a technique that can make website pages *updated* asynchronously. This means that the browser does not need to *reload* the entire web page when there is only a small data change. AJAX will send a request to the server, and continue execution without waiting for a reply from the server first.

## Checklist implementation
1. Create path `/todolist/json` in urls.py with appropriate function to return all task data in json form and use AJAX GET to display data

2. Create `Add Task` button to open a modal with form

3. Create path `/todolist/add` with appropriate funciton to add new task
