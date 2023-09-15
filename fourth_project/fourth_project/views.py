from django.shortcuts import render
<<<<<<< HEAD

def home(request):
    render (request,"templates")
=======
def home(request):
    return render (request,'index.html')
>>>>>>> a149d79d8e4bb7c05d8a6743f4be91421b2d462d
