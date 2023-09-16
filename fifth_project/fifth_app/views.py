from django.shortcuts import render

def contact(request):
    return render (request,'./fifth_app/index.html/', {'author':'Md Anisul Islam', 'age':23, 
        'blog': 'loremipsum2This article revolves around various Django Template Filters one can use during a project. Filters transform the values of variables and tag arguments. Let’s check some major filters.',
        
        "courses" : [
        {
        "id" : 1,
        "course" : "C",
        "teacher" : "Rahim"
        },
        {
        "id" : 2,
        "course" : "C++",
        "teacher" : "Kahim"
        },
        {
        "id" : 3,
        "course" : "Python",
        "teacher" : "Fahim"
        },
        ]}) 
    # writing as a list