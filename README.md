11-01-2024 
------
1)Go to python vebsite (https://www.python.org/downloads/)
2)download the python latest version
3)click on custom installation
4)Give the path where you want to save the folder
5)next next next click all the check box 
6)open the python folder>Scripts 
7)Copy the path 
8)Set the path in env
9)now check the version python --version
done
-----------------------------------------------------
open the project in vs code
1)in the terminal:
 python -m venv anyname(myenv)
-- takes some time 
 need to activating:- myenv\Scripts\activate.bat
--
 cd myenv
--
pip install django
-- python -m dijango version
------------------------------------------------------
15-01-2023
---
>> cd myenv
-- django-admin startproject myproject
it will create the myproject. 
then we need to go into myproject
>>cd myproject
always we use "myproject" directly into the workspace in vscode
then->
-- x.
python manage.py startapp myapp.
here myapp is the folder where we work and creating theprojects.
it creats the myapp folder in the project.
{--in django we will have admin interface wee need to register with models(models.py)--}
-- command to run the server: python manage.py runserver.
the url contains the defalt page of django.
-----
now in myapp create the file named: "urls.py".
paths can be mention by url patterns.
/render module used for rendering the templates.
httpresponse is the module in django used for activating the responses in the website.
*after doing the task in myapp we need to give the path in the views page.
*setting up the function in the views page 
*in url.py we give the path in views.functionname
*after including the views in url.py in myapp.
*go to myproject url.py path('', include(myapp.urls)), its mandatory but only once.
*if we need to run the urls.py file we need to import the views file 
from . import views(.-> same directory that's why we use . here)

