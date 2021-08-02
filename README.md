Bookshelf Display

# Introduction

We use the "BookShelf" project as an example to practice writing the API. It includes the basic requests, GET/POST/PATCH/DELETE. Also, it has the error handlers for 400, 404, 405, 422. The backend files contains the 'test_flaskr.py', which can be used to test each API and lists the errors if it fails.

The API in this project is a REST API. It will return a JSON-encoded response after receive the request in a URL. 

# Get started

## Base url
The Basic URL is `http://127.0.0.1:5000/books`. As we are using our own computer as the server, it starts with `http://127.0.0.1:5000/`. The command line below can display a general data structure:

    curl http://127.0.0.1:5000/books

the response would be like:

```
{
  "books": [
    {
      "author": "Stephen King", 
      "id": 1, 
      "rating": 5, 
      "title": "The Outsider: A Novel"
    }, 
    {
      "author": "Lisa Halliday", 
      "id": 2, 
      "rating": 4, 
      "title": "Asymmetry: A Novel"
    }, 
    {
      "author": "Kristin Hannah", 
      "id": 3, 
      "rating": 4, 
      "title": "The Great Alone"
    }, 
    {
      "author": "Tara Westover", 
      "id": 4, 
      "rating": 5, 
      "title": "Educated: A Memoir"
    }, 
    {
      "author": "Jojo Moyes", 
      "id": 5, 
      "rating": 5, 
      "title": "Still Me: A Novel"
    }, 
    {
      "author": "Leila Slimani", 
      "id": 6, 
      "rating": 2, 
      "title": "Lullaby"
    }, 
    {
      "author": "Amitava Kumar", 
      "id": 7, 
      "rating": 5, 
      "title": "Immigrant, Montana"
    }, 
    {
      "author": "Madeline Miller", 
      "id": 8, 
      "rating": 5, 
      "title": "CIRCE"
    }
  ], 
  "success": true, 
  "total_books": 16
}
```

# Error

If there is not error, the response has a code 200, and the response json:
  ```
  {
    "success": true
  }
  ```
When there is a error, the error code will be generated.This project documents 4XX errors, including 400, 404, 405, 422
 - "400" : Bad request 
      - The server can not understand the syntax. It may due to the syntax error, bad route. For example, using the command line
    ` curl -X PATCH http://127.0.0.1:5000/books/1 -H "Content-Type: application/json" -d '{"rating"}'`
  trigger a 404 error because it does not add the value for the "rating". The response:
      ```
      {
      "error": 400, 
      "message": "bad request", 
      "success": false
      }
      ```

 - "404" : Not found
      - The server undstand the request, but it can not found the resoure (the page) to be found
      ` curl http://127.0.0.1:5000/books?page=3 `
      the response is 
      ```
      {
      "error": 404, 
      "message": "not found", 
      "sucess": false
      }
      ```

 - "405" : Method is not allowed
     The request uses a wrong method. For example, `curl http://127.0.0.1:5000/books/50` is wrong as the handler '/books/<int:id>' only use PATCH. POST, DELETE. It does not offer GET method. The response is 
     ```
     {
      "error": 405, 
      "message": "method is not allowed", 
      "success": false
    }
    ```

 - "422" : Can not process the resource
    - The server understand the request, but it can not process the resource. It may be due to the resource (id=50) does not exist
    `curl -X DELETE http://127.0.0.1:5000/books/50`
    and the response is 
    ```
    {
      "error": 422, 
      "message": "can not process the resource", 
      "success": false
    }
    ```

# Resource endpoint library

## 1. GET books
  The books are organized into two pages, and each page has 8 books. one page can be query with the following command:

    `curl http://127.0.0.1:5000/books?page=1`

  The response is in json file:
  ```
  {
  "books": [
    {
      "author": "Stephen King", 
      "id": 1, 
      "rating": 5, 
      "title": "The Outsider: A Novel"
    }, 
    {
      "author": "Lisa Halliday", 
      "id": 2, 
      "rating": 4, 
      "title": "Asymmetry: A Novel"
    }, 
    {
      "author": "Kristin Hannah", 
      "id": 3, 
      "rating": 4, 
      "title": "The Great Alone"
    }, 
    {
      "author": "Tara Westover", 
      "id": 4, 
      "rating": 5, 
      "title": "Educated: A Memoir"
    }, 
    {
      "author": "Jojo Moyes", 
      "id": 5, 
      "rating": 5, 
      "title": "Still Me: A Novel"
    }, 
    {
      "author": "Leila Slimani", 
      "id": 6, 
      "rating": 2, 
      "title": "Lullaby"
    }, 
    {
      "author": "Amitava Kumar", 
      "id": 7, 
      "rating": 5, 
      "title": "Immigrant, Montana"
    }, 
    {
      "author": "Madeline Miller", 
      "id": 8, 
      "rating": 5, 
      "title": "CIRCE"
    }], 
  "success": true, 
  "total_books": 16
  }
```

## 2. POST books







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