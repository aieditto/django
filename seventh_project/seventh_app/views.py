from django.shortcuts import render

# Create your views here.

def payment(request):
    return render (request,'./seventh_apps/payment.html')

def about(request):
    if request.method == 'POST':
            name = request.POST.get('username')
            email = request.POST.get('email')
            return render (request,'./seventh_apps/about.html', {'name': name , 'email': email})
    else:
            return render (request,'./seventh_apps/about.html', {'name': name , 'email': email})  
         
        # {'name': name, 'email': email} this are dictionary which value is send by pair in python like
        # key : value pair 
    
def form(request):
       return render (request,'./seventh_apps/form.html')
           
        
       
   
        

