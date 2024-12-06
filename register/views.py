from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Custom_user
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username.isdigit() and username != "iliya":
            return render(request, 'login.html', {'error': "شماره تلفن باید به صروت عدد باشد"})
        elif len(username) != 11 and username != "iliya":
            return render(request, 'login.html', {'error': "شماره تلفن باید 11 رقم باشد"})
        if len(password) < 8 :
            return render(request, 'login.html', {'error': "رمز عبور باید بیشتر از 8 کارارکتر باشد"})
        elif password.isdigit():
            return render(request, 'login.html', {'error': "رمز عبور باید به صورت حروف یا ترکیبی از حروف و عدد باشد"})
        else :
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                if not User.objects.filter(username=username).exists():
                    User.objects.create_user(username=username, password=password)
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect("update")
                    else:
                        return HttpResponse("User registered, but login failed.")
                else:
                    return render(request, 'login.html', {'error': 'رمز عبور اشتباه است'})

    return render(request, 'login.html')

@login_required
def update(request):
    if request.method == "POST":
        melicode = request.POST.get('melicode')
        day = request.POST.get('day')
        month = request.POST.get('month')
        year = request.POST.get('year')
        if not melicode.isdigit():
            return render(request, 'login2.html', {'error': "کد ملی باید به صورت عدد باشد"})
        elif len(melicode) != 11 :
            return render(request, 'login2.html', {'error': "کد ملی باید 11 رقم باشد"})
        if not year.isdigit():
            return render(request, 'login2.html', {'error': "سال تولد باید به صورت عدد باشد"})
        elif day > 31 or day < 0:
            return render(request, 'login2.html', {'error': "روز تولد باید بین 1 تا 31 باشد"})
        if not day.isdigit():
            return render(request, 'login2.html', {'error': "روز تولد باید به صورت عدد باشد"})
        if not month.isdigit():
            return render(request, 'login2.html', {'error': "ماه تولد باید به صورت عدد باشد"})
        elif month > 12 or day < 0:
            return render(request, 'login2.html', {'error': "روز تولد باید بین 1 تا 12 باشد"})
        Custom_user.objects.create(melicode = melicode , year = year, day = day , month = month , user = request.user )
        return redirect("home")
    else:
        return render(request, 'login2.html')


def logout_user(request):
    logout(request)
    return redirect("home")