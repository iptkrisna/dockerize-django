from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')


def postgre(request):
    db_data = User.objects.all()
    print("\n*********************>")
    for user in db_data:
        print(user, " => ", user.email)
    print("<*********************\n")
    return redirect('home')