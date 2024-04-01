from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.check_prof:
                return redirect('prof/')
            else:
                return redirect('student/')
        else:
            return render(request, 'login_sys/login_home.html',{'error_message':'Please try again'})
    else:
        return render(request, 'login_sys/login_home.html')