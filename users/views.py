from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from .forms import CustomUserCreationForm as cf

def join(request):
    print(request)

    if request.method == 'GET':
        form = cf()
        return render(request, 'registration/join.html', {'form': form})
    else:
        form = cf(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            print(user, end='\n')
            print(request)

            user.user = request.user  # Set the user object here
            user.save()  # Now you can send it to DB
            return render(request, 'registration/join-complete.html', {'msg': 'successfully joined'})

