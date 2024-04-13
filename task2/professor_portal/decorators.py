from django.shortcuts import render

def professor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_prof:
            return render(request,'login/login.html')
        return view_func(request, *args, **kwargs)
    return wrapper