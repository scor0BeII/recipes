from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipes
from .forms import RecipesForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    return render(request, "index.html")
def who_are_you(request):
    return render(request, 'home_screen.html')
def recps(request):
    title = request.GET.get("query")
    if title:
        recipes = Recipes.objects.filter(title__icontains=title)
    else:
        recipes = Recipes.objects.all()
    context = {"recipes" : recipes}
    return render(request, "recipes.html", context)
@login_required(login_url=reverse_lazy("login"))
def forms(request):
    if request.method == "POST":
        form = RecipesForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = Recipes(**form.cleaned_data)
            recipe.user = request.user
            recipe.save()
            url = reverse("login")
            return redirect(url)
    else: 
        form = RecipesForm()
    context = {"form" : form}
    return render(request, "entry.html", context)
# Create your views here.
