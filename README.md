# ZyTyLyChallenge
Challenge code for a library app, backend made in Python, MySQL (provided by evaluator), RestApi and Docker


We should be able to docker run <image> and have your app server up and running waiting for connections to its endpoints.

The code must use just these variables:
ADMIN_API_KEY	The secret API key used to call the admin endpoints (the key that goes into the Authorization header of some API requests)
API_LISTENING_PORT	The port on which your API needs to listen for HTTP requests
DB_HOST	The hostname of the database your app needs to connect to
DB_NAME	The name of the database
DB_PASSWORD	The password of the database
DB_PORT	The port of the database
DB_USERNAME	The username of the databas

Define User Registration, User Login and handle errors/exceptions
Book Request, Update, Delete Books from Book List and handle erros/exceptions
Borrow Book and ensure no book can be borrowed by another user and the user cannot exceed 5 borrowed books
