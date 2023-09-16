from django.shortcuts import render

def contact(request):
    return render (request,'./fifth_app/index.html/', {'author':'Anis', 'age':23, "courses" : [
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