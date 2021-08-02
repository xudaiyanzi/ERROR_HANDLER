# Bookshelf
This project uses a virtual bookshelf to create, update, delete, and query books in BOOK database. From the practical purposes, the databases has a few books in place. With the provided API, one can manipulate the bookshelf as needed.

## 1. Getting started
We need to install the backend and frontend before using the bookshelf. 

  ### 1.1 Backend installation
  There are three parts of the backend need to be take care of.

  #### ==> 1.1.1 Install the requirements.txt
  We need first `cd` to the `backend` directory and use the command line `pip3 install -r requirements.txt` to install all the prerequisities

  #### ==> 1.1.2 Install the database and create tables
  We use the psql to manipulate the database, and we first create the database and then create tables in the database:

  #### ==>  ==> 1.1.2.1 Install the database
  Mac users first start the postgres server. Use the command line: 
        `which postgres`
        `postgres --version`
  to check the version of postgres and then use
        `pg_ctl -D /usr/local/var/postgres start`
  and 
        `pg_ctl -D /usr/local/var/postgres stop`
  to start and end the post gregre server

  Following the step above, we open the postgres using 
        `psql postgres` 
  and install the basebase using 
        `\i setup.sql`
  We need to `\q` to exit the psql before install the tables.

  #### ==>  ==> 1.1.2.2 Install the tables
  In order to create the tables, we (MAC user) use
         `psql -f books.psql -U student -d bookshelf`

  #### ==>  ==> 1.1.3 Run the flask
  If we want to launch the bookshelf, we `cd` to the `backend` directory and use: 
        `export FLASK_APP=flaskr`
        `export FLASK_EVN=development`
        `flask run`

  we can either go to the `http://127.0.0.1:5000/ANY_API_ENDPOINT` or use the `curl` to see the API responses.

### 1.2 Frontend installation
  There are three parts of the backend need to be take care of.

## 2. API Reference

We use the "BookShelf" project as an example to practice writing the API. It includes the basic requests, GET/POST/PATCH/DELETE. Also, it has the error handlers for 400, 404, 405, 422. The backend files contains the 'test_flaskr.py', which can be used to test each API and lists the errors if it fails.

The API in this project is a REST API. It will return a JSON-encoded response after receive the request in a URL. 

### 2.1 Getting started

#### Base url
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

### 2.3 Error handler

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

### 2.4 Resource endpoint library

#### 2.4.1 GET books
##### GET books by page
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

#### 2.4.2 PATCH books
When it is needed to update the bookshelf, we use the patch method. The request should include the id of the resource and the attribute to be updated. For example,
` curl -X PATCH http://127.0.0.1:5000/books/1 -H "Content-Type: application/json" -d '{"rating":5}' `

The response is 
```
{
  "id": 1, 
  "success": true
}
```

#### 2.4.3 POST method

##### 2.4.3.1 Add a new entry
This method is used to added an entry (a book). We use 
`curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"title":"Neverwhere", "author":"Neil Gaiman", "rating":"5"}'`

The response is 
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
  "created": 23, 
  "success": true, 
  "total_books": 17
}
```

##### 2.4.3.2 search the book by title
If one needs to search a book. The following command can be used:
` curl -X POST http://127.0.0.1:5000/books -H "Content-Type: application/json" -d '{"search":"the"}'`

The response is 
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
      "author": "Kristin Hannah", 
      "id": 3, 
      "rating": 4, 
      "title": "The Great Alone"
    }, 
    {
      "author": "Rachel Kushner", 
      "id": 15, 
      "rating": 1, 
      "title": "The Mars Room"
    }, 
    {
      "author": "Gregory Blake Smith", 
      "id": 16, 
      "rating": 2, 
      "title": "The Maze at Windermere"
    }
  ], 
  "success": true, 
  "total_books": 4
}
```

#### 2.4 Delete a book
To delete a book, we use the DELETE method. The command line is
` curl -X DELETE http://127.0.0.1:5000/books/23?page=3 `

The response is 
```
{
  "books": [], 
  "deleted": 23, 
  "success": true, 
  "total_books": 16
}
```

The attribute books shows the book on that particular page.

## 3. Deployment

## 4. Authors

## 5. Acknowledgement




