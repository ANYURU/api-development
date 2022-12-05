Learning Django. 
Some notes I take during the learning process.
Web framework: Collection of modules, packages and libraries designed to speed up development.
Other Frameworks
- Flask
- Cherry Pie
- Web2py
- Pyramid

MVT Design Pattern. 
Django follows the MVT design pattern. 
- Model - Data Access Layer
- Template - Presentation Layer
- View - Business Logic

Process
- Created a virtual environment. So that we can isolate the concerns of the project from the entire system.  
- Activated the virtual environment and installed django. 
- Use command: django-admin to see the administrator commands that we can run. 
Some of the commonly administrator commands are:
- Make migrations
- Migrate
- Run server
- Start server
- Start project

django-admin startproject <projectname>
cd <projectname>
python3 manage.py runserver

<!-- Files to work with inside our project: We will be working with the settings files and the url file. The Django Application is made up of a series of smaller applications. -->

Django Templating engines and using template tags

