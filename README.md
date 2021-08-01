Bookshelf Display

# Introduction

We use the "BookShelf" project as an example to practice writing the API. It includes the basic requests, GET/POST/PATCH/DELETE. Also, it has the error handlers for 400, 404, 405, 422. The backend files contains the 'test_flaskr.py', which can be used to test each API and lists the errors if it fails.

The API in this project is a REST API. It will return a JSON-encoded response after receive the request in a URL. 

# Get started

## 1. base url
The Basic URL is 'http://127.0.0.1:5000/books'. As we are using our own computer as the server, it starts with "http://127.0.0.1:5000/". 

    -- the command line below can display a general data structure:

    "$curl http://127.0.0.1:5000/books"


2. The books are organized into two pages, and they can be query, use the command line:
    "$curl http://127.0.0.1:5000/books?page=1"
    and 
    "$curl http://127.0.0.1:5000/books?page=2"

3. 






# API Documentation Practice
In this exercise, your task is to practice writing documentation for the bookstore app we created earlier.

You'll soon be writing documentation for your final project (the Trivia API), after which you'll get feedback from a reviewer. You can think of this as some rudimentary practice to prepare for that.

At each step, you can compare what you've written with our own version. Of course, **there isn't a single correct way to write a piece of documentation**, so your version may look quite different. However, there are principles and practices you should follow in order to produce quality documentation, and we'll point this out so you can check whether you've incorporated them in what you wrote.

## Getting started
Now, add a Getting Started section to your documentation. Remember, this should include at least your base URL and an explanation of authentication. Feel free to provide other information that is relevant for your API


## Error Handling
Now, add an Error Handling section to your documentation. It should include the format of the error responses the client can expect as well as which status codes you use.
- Response codes
- Messages
- Error types

## Endpoint Library
Now, add an Endpoint Library section to your documentation. Make sure that endpoints, methods and returned data are all clear. Consider including sample requests for clarity

- Organized by resource
- Include each endpoint
- Sample request 
- Arguments including data types
- Response object including status codes and data types 