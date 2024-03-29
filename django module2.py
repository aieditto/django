                            "Module-1.7 to" 
#How to create environment, install jango, project and apps and connect between them

#Create Environment:
    
1. pip install virtualenv
2. virtualenv add_a_room(like room1)
3. source ./room1/Scripts/activate
4. To check correct or not (virtualenv --version)

#install django:
1. pip install django
2. python -m django --version (to check django)

#Create Project:
1. django-admin startproject project_name
2. cd project_name
3. python manage.py runserver
#the it will show a link and click on that after that
#a webpage will open

#if i want to write there something the following steps
1. cd project_name
#2. The create a file with the name of views.py because
#there are no views.py to show the template or other thing
#3. search the urls.py and write there 
    1. from .import views
    2. path('', views.home),

#4. For connecting with the urls page now i have to import
 # so write this code
    from django.http import HttpResponse

  #  then write a function
    def home(request):
        return HttpResponse('From Home of the main project')
        
   #     (HttpResponse is use for sending the response because a webpage 
    #    cant understand the return )

# Why we create apps?
# We create apps for distributing the project code
# it will help to run the code faster, understandable also
# less time consume etc.


"Module 1.8 Creating An App"

#Create Apps:

1. django-admin startproject project_name
2. cd project_name
3. django-admin startapp app_name

#** if i want to write there something the following steps:

# 1. Create a file with the name of app_name views.py because
# there are no views.py to show the template or other thing

#3. search the urls.py and write there 
    1. from .import views
    2. path('', views.home),
#4. For connecting with the urls page now i have to import
 # so write this code
    from django.http import HttpResponse

#    then write a function
        def home(request):
        return HttpResponse('From Home of the main project')
        # (HttpResponse is use for sending the response because a webpage 
        # cant understand the return )

3. python manage.py runserver
# the it will show a link and click on that after that
# a webpage will open


" module 2.4- how to write html code from template"

# 1. first create a project. then create a views.py name file
# 2. Goto urls. py and make connection between views.py

   from .import views
   path('', views.home),

3. Then create templates folder on third project 
    goto settings to declare goto template format: 
    write this 'DIRS': [BASE_DIR/'templates'],

4. Goto views.py and write
    from django.shortcuts import render
    def home(request):
    return render(request,'index.html')
5. Goto index.html file write code here and run..

"            Module-2.6. Django Template Language If-Else condition"
# after the setting of apps template now from the views.py in the function there are a link like 

# ./app_name/index.html or something write there with comma like the below example:
    
    return render (request,'./fifth_app/index.html/', {'author':'Anis', 'age':23})

# I can send value from here it will be shown by template folder index.html file

# Now you can write condition here like the below example:

    {%if age < 10 %}
    <p>you are dumb</p>
    {% else %}
    <p>you are nah</p>
    {% endif %}

# NB: if you write *if* condition you have to must be write *endif* there
                
                "Module 2.7 For loop " 

# for running the for loop first I have to take data from views.py there are a function
# that function store the value and share with the template file use this function 

{% for how_many_time_runs in the_stored_variable %}
    # the other codition write here
{% endfor %}

# For Example:

{% for i in count %}
    <p>{{i.id}}</p>
    <p>{{i.id}}</p>
    <p>{{i.id}}</p>
{% endfor %}

                           " Module 2.8 Filtering

# Filtering means some values are passing from the views.py so If we need to change any word, change or collect
# any information then we can use filtering which are the feature of DTL (Django Template Language) where I can
# write python code in html thats magic for more : https://www.geeksforgeeks.org/django-template-filters/

# how to write filter:

{{ variable_name | filter_name }}

# For Example:
{{ value | length }}
If value is [‘a’, ‘b’, ‘c’, ‘d’], the output will be 4.

    <p>
       Character of Name: {{author | length}}
       <br>
       Character of Name: {{author | upper}}
    </p>

# NB: The value must need to passed from the views.py 
# Character of Name: {{author | length}}
       
       <br>
       Character of Name: {{author | upper}}
       <br>
       <br>
       truncatewords are usually use for compressing the sentence or topic like see more continue etc.
       <br>
       blog truncatewords:<br>
       {{blog | truncatewords:5}}
               
               
               
               
        "        Module-3.1
# There are two types of files. 1. Static File, 2. Dynamic file

# Static files means that file which are store on main project and static files elements cant be changes.


"Working with Static Files inside Project"
"Static file means  song, image, video or other thing which are 
"store in main project and they are unchangeable.
"So, What is the procedure?
"First of all 
step 1: create a folder with name static or something
step 2: crete other folder under the static folder to store
        images, js and css folder
step 3: then take some image copy that and paste it images folder
step 4: if we try to access images django didnt allow that so it need 
        to be take permission from main project setting folder"

        after that we can see **** STATIC_URL='static/'

       """" this means if we have a website with the name of abc.com then if we need
        to access image from images folder then the link will be: static.abc.com
        this means the file is on static folder and it communicate with STATICFILES_DIRS 
        to locate the file.

        Your project will probably also have static assets that aren’t tied to a 
        particular app. In addition to using a static/ directory inside your apps, 
        you can define a list of directories (STATICFILES_DIRS) in your settings 
        file where Django will also look for static files. 
        this means this STATICFILES_DIRS use for where the images file are store For example:""""

        **** STATICFILES_DIRS = [
                 BASE_DIR / "static",
              ]
    # then goto html folder and try to link the images
    {% load static %} #load static means loading the static folder
    <img src="{% static 'image_link' %}" alt="">
    <link rel="stylesheet" href="{% static 'link'%}">



                         "Module 3.2 Static folder run from app

        almost same as the project

        

                        " Module 3.3 Static vs Dynamic file/ Media File

# Media file is changeable when a data come from
# backend that is media file. 

# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored'
MEDIA_ROOT = BASE_DIR / 'media'
        
        # By default, Django doesn't serve media files during development( when debug=True).

        # In order to make the development server serve the media files open the url.py of the project and make the below changes.
url.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    ...]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

"That's all now, run the local development server add files in the media root folder and retrieve them from media URL.

                
                        
                       " Module 3.4. Adding Bootstrap

                            Copy paste from website


               " Module 3.5 Using Url tag in Django Project

path('data/',views.data, name ="information"), 
# to make url tag shortcut i have to give a name of the main source link like as a information

# then goto template folder and goto html file write there
# on a linke like :

<a href = "{% url 'information' %}"> Data </a>


                "Module 3.6 Inheritence in Django Project

# If i need to do same work repeatedly it will tough for me and It will make the website slow
# so we have to use inheritance method for doing this.

# The html file name must be base.html
# Inheritance means the way of how a child template hold all the characteristics of parent template
# DRY principle (Dont Repeat Yourself)

For Example: 
                              --- About.html  
Navigtion Bar (Base.html)  ---|-- index.html
                              --- feedback.html

                Extends Tag
  {% extends "parent_template_name" %}

                Block Tag
{% block blockname %} other instruction {% endblock %}

For Example:
    from: index.html
    {% extends 'base.html'%}
    {% block article %} hello world {% endblock %}
    {% block content %} {{block.super}} The code write {%endblock%} //super keyword use for merging with parent

    from: base.html
    <html>
        <head> <title></title> </head>
        <body>
            <h1> {% block article %} {% endblock %} </h1>
            <h1> {% block content %} in python {% endblock %} </h1>
        </body>
    </html>


"                    Module 4.1 Working with Html Forms in Django

# First create a html forms on template folder. Then connect with base.html for DRY(Dont Repeat Yourself) 
# principle for avoiding repeat code. Then goto forms file and create a form there.
# After that when adding a method in <form> tag like

                        <form method='post'>

# then there will be show CSRF error. This is a security token and the full form of CSRF is (Cross Site Request Forgery)

# and it is said to occurs when a malicious Web site deceives users into unwillingly and unknowingly loading a URL from a site where they've previously been authenticated, thus exploiting their status and also putting the data at risk.

# POST usually use for collect data send that data to the server and this is encrypted. Thats Why
# this are use for storing personal info.

# GET use for collecting data and showing others which have no harmful information or personal information.

# after that add after the form tag 

                    
                {% CSRF_token %}

# then goto  views.py of the apps and write there on form function. 
    
                print(request.POST)

when I entry some info on form this data send to the backend but it will show some string that is no understandable
thats why I have to goto 
        
        form.html--> search where the input are taking information write there name='username', email='email' this are like
        catching the value of send from front end. and then it will show the info at terminal.

        # 1. then write a condition on a function

             if request.method=="POST/GET": //POST use for privacy beacuse it cant show on link but GET do
                name=request.POST.get('username')  
                email=request.POST.get('email')  
                return render (request,'./seventh_apps/about.html', {'name': name, 'email': email})
            else: 
                return render (request,'./seventh_apps/about.html', {'name': name, 'email': email}) 

        # 2. go to that form.html and write there catch the value which are pass on previous line 

            <h1>Name{{name}}</h1>
            <h1>Email{{email}}</h1>
            
            # after running it will show the value 
            # but
            # if I want to show this on other page then I have to copy all condition
            # and paste it on that function which have a link with the page
            # and then goto on the page write there the given upper code.

            # then goto form.html beside the <form> tag write there action=/...../ 
            # it will work perfectly.

            # the process are same for other input to handling data from form.

            # If GET use as a method the value will show on the link and it will breache the security
            # hacker can easily hack information.  



$#$@#@ Project form handling &*#@#@ 

                    "4.3 Introduction to Django Built in Forms
# How to create FORM api where no need to write html file just django 
# Step: 1
# First create a file with the name of **** forms.py **** this is use for 
# then write there

from django import forms                        # Importing necessary module 'forms' from the Django framework
class ContactForm(forms.Form):                  # Defining a class 'ContactForm' which inherits from 'forms.Form'
    name = forms.CharField(label="Username")    # Defining a field 'name' of type CharField with a label "Username" 
    email = forms.EmailField()                  # Defining a field 'email' of type EmailField
    
Step-2: 
Goto urls.py and write there 

path('django_form/',views.django_form,name="django_form")   #this are connecting with the views.py 

Step-3:
Goto views.py and  write there 
from . forms import ContactForm     #here ContactForm are importing from the forms.py
def django_form(request):   #function define
    form = ContactForm()  #contactform value are store here
    return render (request,"django_form.html",{'form':form})  #then return to django_form.html

Step-4:
Goto  templates folder -> create a html folder named "django_form.html"

write There
write a html code
<form method="POST">
{% csrf_token %}
{{form}}            //this are passing the value from views.py
{{form.as_p}}  //as_p use for paragraph setting
<button class="btn btn-outline-success" type="submit">Submit</button>
</form>

Now.....
to show the value which are input from the frontend

 if request.method == 'POST':
        book = BookStoreForm(request.POST)  #to show the value from website write here between the braces  request.POST
        if book.is_valid():
            print(book.cleaned_data)
            book.save(commit=False)
    else:
        book = BookStoreForm()
# form = ContactForm(request.POST) 
#     if form.is_valid():   // if any value are submited then it will be true and print that 
#         print(form.cleaned_data)



                        "Module  4.4 Adding Crispy Forms in Django

To add bootstrap  theme we need to install crispy forms first

first install this: pip install crispy-bootstrap5
then goto settings.py and add these on installed app

    "crispy_forms",
    "crispy_bootstrap5",

then goto that html file which are added as form
so goto there  and write

<form method="POST">
    {% load crispy_forms_tags %}   //importing crispy_forms_tags
    {% csrf_token %}
    {{form | crispy }}  // this thing add crispy with the form
     <!-- {{form.as_p}} -->
     <button class="btn btn-outline-success" type="submit">Submit</button>
 </form>


                    "Module 4.5 and 4.6 Some Built in FormFields Part 1 and 2

  name=forms.CharField(label="Username")
    email=forms.EmailField()
    age=forms.DateField()
    check =forms.BooleanField()
    FOOD= [('B','Burger'),('M','Momos'), ('Bir','Biriani')]
    food=forms.MultipleChoiceField(choices=FOOD)


            
            
            
            "Project: model_practice

""""Module 5.1 Introduction to Django Models""""

# ORM (Object Relational Mapper) is a technique that helps to interect 
# between database such as SQL, MYSQL, SQlite, Oracle

# QuerySet: A list of object that helps to create a database that is called QuerySet.

                        MODEL
# Model contain essential fields and behaviors of the data.
# each model maps to a single database table.

# Model class is a class which will represent a table in database.



                        "Module 5.2 Creating a Model in Django

# to creating a model or database
# we need to follow these steps :
# Write  our code inside models.py file

from django.db import models

class class_name(models.Model):
    field_name = models.field_type()
    for example:
    name = models.CharField(max_length=20)
    roll = models.IntegerField()                // for integer no value need

then run on terminal:
        $ python manage.py makemigrations   # this command will generate the sql query according to your
        $ python manage.py migrate          # model definition then it will apply those queries into your database
                                            # defined model into another folder named
                                            # migrations under app directory
        $ python manage.py migrate

        this will create a file on migrations folder. 

""""5.3 manual way by software""""

"5.4 Creating Superuser and Accessing Admin Panel

# to enter admin panel  we have to create super user first then access it.
$python manage.py createsuperuser

user: aieditto
pass: md123698741

# to show the model to admin panel on website
# open admin.py file from /admin/app
# and add following line of code

goto admin.py

# then write there: 

from .import models
admin.site.register(models.model_name)

# then goto website you can see that.
# If you want to show  all fields in admin panel then just use:

def __str__(self):
    return self.name
    this is a method which returns string representation of object.
    and it write on **** models.py ****



      "          Module 5.5 Showing Model data to frontend

# If you want to show your data to the front end as a table
# you need to make some changes in views.py
# views.py :
First,
import render from django.shortcuts import render
then,
    write: 
    from .import models  #because i have to import the models

#    after that need to take a variable:
                            variable_name= models.models_name.objects.all()

                            # here  objects means get all records from database
                            # Then pass it into template using render function like

# then if you need to show the  data in terminal you can print that by 
 print(variable_name)

Second,
     return render(request,'home.html',{'variable_name':variable_name})

     // return the variable as a list

Third,
    # go to template file and write there:
    {% if variable_name %} //if student variable has any data then goto next step

    {% for i in variable_name_of_model_variable %}
    <tr>
        <td>{{i.name}}</td>
        <td>{{i.roll}}</td>
        <td>{{i.mobile}}</td>
        <td>{{i.subject_name}}</td>
        <td>{{i.fathers_name}}</td>
    </tr>
    {% endfor %}
    {% else %}
    {% endif %}



"Module 5.6 Deleting Model Data From Frontend

# on home.html write there with anchor tag:

<td><a type="button" class="btn btn-danger" href="">Delete</a> </td>

# then go to views.py and write there a function 

def delete_student(request,roll)                    #roll are the primary key thats why to make a link                                 
    student_delete = models.Student.objects.get(primary_key = roll)  
    print(student_delete)
                                                 """"
                                                 models.Student: Refers to the Student model defined in Django's models.py file.
                                                .objects: Represents the manager through which database queries are performed on the Student model.
                                                .get(primary_key=roll): This method retrieves a single Student object from the database where the value of the primary key field (primary_key) matches the value of roll.
                                                It's assumed that primary_key is the name of the primary key field in the Student model.
                                                In summary, this lin fetches a single Student object from the database based on the value of its primary key (roll).""""
then,
# goto  urls.py and write there

path('delete_student/<int:roll>',views.delete_student, name='delete_student')

again goto views.py

write 
from django.shortcuts import render, redirect

def delete_student(request, roll):
    student_delete=models.Student.objects.get(pk= roll).delete()
    # students=models.Student.objects.all()
    print(student_delete)
    # return render (request,'home.html',{'students':students})
    return redirect('homepage')


                                "5.7 Introduction to Model Form in Django

Meta class is kind of nested class
to change the behavoiur of other class Meta class is used 

                                "5.8 Creating form using Model Form

# important and shortcut:      
# **********    you can shortcutly call link                                  ********
# **********                                                                  ********
**********  from first_app.views import home, delete_student, many more...  ********
# *********************************************************************************
# <<<<<<< HEAD


=======
create file name with forms.py then goto  forms.py
after that write there

from django import forms  //importing forms  module
from second_app.models import  StudentModel  //importing StudentModel from the models.py file 
now,
    create a modelform class  inside the forms.py by writing below code :
     
     class StudentForm(forms.ModelForm):
        class Meta:             //#meta class use for writing the characteristics of other class
            model = StudentModel   #//linking our data base table with this class
            fields = '__all__'     #//it will show all field of the database table in
            or
            fields= [
                'roll', 'name', 'fathers_name', 'contact_number'
            ]
            
        labels={
            'roll' : "Roll Number",
            'name' : 'User Name',
            'fathers_name':"Father's Name",
        }
        widgets={
            'roll' : forms.TextInput(attrs={'class' : 'btn-primary'}),
            'name': forms.PasswordInput()
        }
         help_texts={
            'name':'This is the username of user',
            'roll':'Confirm your roll'
        }
        error_messages={
            'name': {'required':'your name is required'}
        }



'   Module-6-Book Store project

        editing data:
            
            why instance use?
            instance use for to catched the data from the model through any id or identity

"views.py
                    from django.shortcuts import render, redirect
                    from book.forms import BookStoreForm  # Importing the BookStoreForm from forms.py
                    from book.models import Bookstoremodel  # Importing the Bookstoremodel from models.py
                    # Create your views here.
        'This function use for storing data from the form
                    def store_book(request):
                        if request.method == 'POST':  # Checking if the request method is POST
                            book = BookStoreForm(request.POST)  # Creating a BookStoreForm instance with POST data
                            if book.is_valid():  # Checking if the form data is valid
                                book.save()  # Saving the form data to the database
                                print(book.cleaned_data)  # Printing cleaned form data to console
                                return redirect('show_book')  # Redirecting to the 'show_book' URL
                        else:
                            book = BookStoreForm()  # Creating a blank BookStoreForm instance for GET requests
                        return render(request, 'store_book.html', {'form': book})  # Rendering the form in the template
        
        'This function use for showing the data from the form
                    def show_book(request):
                        books = Bookstoremodel.objects.all()  # Querying all Bookstoremodel objects from the database
                        return render(request, 'show_book.html', {'books': books})  # Rendering the books in the template


        'This function use for editing the data which are already store on model database
                    def book_edit(request, id):
                        book_model = Bookstoremodel.objects.get(pk=id)  # Getting a specific Bookstoremodel object by primary key (id)
                        book_form = BookStoreForm(instance=book_model)  # Creating a form instance with existing model data
                        if request.method == 'POST':  # Checking if the request method is POST
                            book = BookStoreForm(request.POST, instance=book_model)  # Creating form instance with POST data and existing model instance
                            if book.is_valid():  # Checking if the form data is valid
                                book.save()  # Saving the updated form data to the database
                                print(book.cleaned_data, f'data has been updated')  # Printing cleaned form data to console
                                return redirect('show_book')  # Redirecting to the 'show_book' URL
                        return render(request, 'store_book.html', {'form': book_form})  # Rendering the form in the template

        'This function use for deleting the data which are already store on model database
                    def delete_data(request, id):
                        book_model = Bookstoremodel.objects.get(pk=id)  # Getting a specific Bookstoremodel object by primary key (id)
                        book_model.delete()  # Deleting the specific Bookstoremodel object from the database
                        return redirect('show_book')  # Redirecting to the 'show_book' URL after deletion


"urls.py: 
            from django.urls import path

            from book.views import store_book,show_book,book_edit,delete_data

            urlpatterns=[
                path('',store_book,name='store_book'),  
                path('show_book/',show_book,name='show_book'),
                path('book_edit/<int:id>',book_edit, name='book_edit'), 
                path('delete_data/<int:id>',delete_data, name='delete_data')  
            ]
            

'models.py:
                from django.db import models

                class Bookstoremodel(models.Model):
                    CATEGORY = [
                        ('Thriller', 'Thriller'),
                        ('Comics', 'Comics'),
                        ('Romantic', 'Romantic'),
                        ('Educational', 'Educational'),
                        ('Sci-fi', 'Sci-fi')
                    ]
                    id = models.IntegerField(primary_key=True)
                    book_name = models.CharField(max_length=30)
                    author = models.CharField(max_length=30)
                    category = models.CharField(max_length=30, choices=CATEGORY)
                    first_pub = models.DateTimeField(auto_now_add=True)
                    last_pub = models.DateTimeField(auto_now=True)
                    
                    def __str__(self):
                        return f'ID: {self.id} , Author: {self.author} '

'forms.py:
                from django import forms
                from book.models import Bookstoremodel
                class BookStoreForm(forms.ModelForm):
                    class Meta:
                        model=Bookstoremodel
                        fields= [
                            'id',
                            'book_name', 'author', 'category'
                        ]
                        
'admin.py:
                    from django.contrib import admin
                    from book.models import Bookstoremodel

                    # Register your models here.
                    admin.site.register(Bookstoremodel)