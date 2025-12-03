from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from products.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def index(request):
    products = Product.objects.all()
    return render(request, 'home/index.html', {
        "products": products
    })


@login_required
def profile(request):
    return render(request, 'home/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
