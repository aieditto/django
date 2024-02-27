from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    return render (request,'contact.html')

def form(request):
    return render (request,'form.html')

def form_data(request):
    print(request.POST)
    if request.method=='get':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request,'form_data.html',{"name":name, "email":email})
    else:
        return render(request,'form_data.html')