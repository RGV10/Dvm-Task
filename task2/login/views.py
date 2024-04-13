from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('professor_portal/')
            else:
                return redirect('student_portal/')
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid login info.'})
    else:
        return render(request, 'login/login.html')
