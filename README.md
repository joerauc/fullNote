Full stack note taking application which using a REST API and JWT tokens to enforce authorization and restrict notes access to their authors.

To spin up the app:
Download and unzip the application. Open your code editor to the folder where you installed the files and activate the virtual environment.

Install all project dependencies:
```pip install -r requirements.txt```

Change directories into the backend folder and spin up the backend:
```python manage.py startapp```

Split your terminal. In the new terminal, change directories into the frontend, and install frontend technologies:
```npm install axios react-router-dom jwt-decode```

Spin up the frontend server:
```npm run dev```

If that doesn't work, run the following line:
```npm install```
Then try to start the frontend again.

Follow the link to open the frontend. Change the URL according to what you're looking to do.
Register an account:                http://127.0.0.1:5173/register
Login:                              http://127.0.0.1:5173/login
Logout:                             http://127.0.0.1:5173/logout
Home page (authorized users only):  http://127.0.0.1:5173/

Please note!
This application is still in progress. It is possible for a user to register, login, and logout. Unauthorized users will be rejected. Website design and note taking, however, have not yet been implemented.

Technologies used: Python, Django, REST, React, JavaScript, JWT