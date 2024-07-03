from django.shortcuts import redirect, render
from item.models import Category, Item
from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html', {
		'categories': categories,
		'items': items,
	})

def contact(request):
    return render(request, 'core/contact.html')


def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {
		'form': form
	})