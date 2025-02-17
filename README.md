Full stack note-taking application using a REST API and JWT tokens to enforce authorization and restrict notes access to their authors.


To spin up the app:
Download and unzip the application. Open your code editor to the folder where you installed the files and activate the virtual environment.

Install all project dependencies: <br />
```pip install -r requirements.txt```

Change directories into the backend folder, then spin up the backend: <br />
```python manage.py startapp```

Split your terminal. In the new terminal, change directories into the frontend, then install frontend technologies: <br />
```npm install axios react-router-dom jwt-decode```

Spin up the frontend server: <br />
```npm run dev```

If that doesn't work, run the following line: <br />
```npm install``` <br />
Then try to start the frontend again.

Follow the link to open the frontend. Change the URL according to what you're looking to do. <br/>
Register an account:                http://127.0.0.1:5173/register <br/>
Login:                              http://127.0.0.1:5173/login <br/>
Logout:                             http://127.0.0.1:5173/logout <br/>
Home page (authorized users only):  http://127.0.0.1:5173/

Technologies used: Python, Django, REST, React, JavaScript, JWT