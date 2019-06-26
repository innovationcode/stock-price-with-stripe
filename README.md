# Stock-price(Back-end and Front-end)

Back-end as well as Front-end repo for labs13-Stock-price

# API Documentation

#### App delpoyed at [HEROKU](https://stock-price-stripe.herokuapp.com/) <br>

## Getting started
The complete application is build with Flask which is a microframework for Python based on Werkzeug, Jinja 2. 
<br>

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

To get the server running locally:

- Clone this repo <br>
$ git clone https://github.com/labs13-stock-price/backend.git <br>
$ cd backend <br>

- Install the dependencies: <br>
$ pip install -r requirements.txt <br>

- Run the development server: <br>
$ python run.py <br>

- Navigate to http://localhost:5000 <br>

### Flask Flexibility

- Flask provides developers generous flexibility for developing their web applications.<br>
- The official documentation is very thorough, providing lots of details with well-written examples.<br>
- Flask is arguably one of Python’s most popular web frameworks, with plenty of tutorials and libraries available to add to   your apps.<br>
- Flask is a lightweight framework with few dependencies. It takes just a few lines of Python to load Flask, and because it is    modular, you can restrict the dependencies to suit your needs.<br>
- Integration with database toolkits like SQLAlchemy, SQL databases like SQLite and MySQL, and NoSQL databases like    DynamoDB and MongoDB is relatively easy.<br>

## App

All server routes located within app directory- views.py

#### Endpoints

------------------------------------------------------------------------------------------------------------
| Method| Endpoint                 | Access Control | Description                                        |
| ------| -------------------------| ---------------| -------------------------------------------------- |
| GET   | `/index`                 | User           | Basic route to render `index.html` Home page       |
| GET   | `/register`              | User           | Renders `register.html` form for new registration. |
| POST  | `/register`              | User           | Accepts user credentials to register new user and update db User-table with hash-passwprd        |
| GET   | `/login`                 | User           | Renders `login.html` form for login                |
| POST  | `/login`                 | User           | User can login using his/her own credentials       |
| GET   | `/reset_password_request`| User           | Renders `reset_password_request.html` form for password reset request |
| POST  | `/reset_password/<token>`| User           |               |
| GET   | `/herokuapp`             | User           | Free as well as paid user can see stock-price sentimental analysis    |
| GET   | `/premium`               | User           | User can update as a premium user -pay and access data to decide right time to sell and buy              |
|       | `/pay`                   | User           | used `stripe` payment to accept the payment        |
|       | `/google_url`            | User           | User can login using his/her GOOGLE credentials    |
|       | `/github_url`            | User           | User can login using his/her GITHUB credentials    |
|       | `/twitter_url`           | User           | User can login using his/her TWITTER credentials   |
| GET   | `/contact`               | User           | renders `contact.html` form for contacting stock-price team  |
| POST  | `/contact`               | User           | accepts data from user and sends e-mail to stock-price mail-id |
------------------------------------------------------------------------------------------------------------

# Data Model

### App User Table

-------------------------------------------------------------------
| Name          | Data type     | Primary Key | Unique | Not NULL |
| ------------- |:-------------:|:-----------:|:------:|:--------:|
| id            | Interger      | +           | -      | -        |
| username      | String        | -           | +      | +        |
| email         | String        | -           | +      | +        |
| password_hash | String        | -           | -      | +        |
| premium_user  | Boolean       | -           | -      | -        |
-------------------------------------------------------------------

## Flask and Flask-extensions 
[Flask Documentation](http://flask.pocoo.org/docs/)

These are the listed Flask-extensions used in this project
- `Flask-login` - Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users' sessions over extended periods of time.
- `Flask-sqlchamy` - 
- `Flask-mail` - 
- `Flask-dance` - 

[Flask Extensions](http://flask.pocoo.org/extensions/)

## Environment Variables

In order for the app to function correctly, the user must set up their own environment variables.

create a config.py(DON'T FORGET TO ADD IT TO `.gitignore`) file that includes the following:

    * SECRET_KEY
    * SQLALCHEMY_DATABASE_URI
    * SQLALCHEMY_TRACK_MODIFICATIONS = False
    * LOG_TO_STDOUT 

    * STRIPE_PUB_KEY `this is generated in the Stripe dashboard`
    * STRIPE_SECRET_KEY `this is generated in the Stripe dashboard`

    * GITHUB_CLIENT_ID 
    * GITHUB_CLIENT_SECRET

    * GOOGLE_CLIENT_ID
    * GOOGLE_CLIENT_SECRET

    * TWITTER_ 
    * TWITTER_ 
 
    * ADMINS 
    * MAIL_SERVER
    * MAIL_PORT 
    * MAIL_USE_TLS
    * MAIL_USERNAME 
    * MAIL_PASSWORD
    

See [Data Science](🚫link to your DS readme here) for details on the fronend of our project.

