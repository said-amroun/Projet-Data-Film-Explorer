from django.shortcuts import render
from films.models import Film
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Film2

def films04_db(request):
    films = Film.objects.all()
    return render(request, "films02_list.html", {"films": films})

# Create your views here.
from django.http import HttpResponse
def film_list(request):
    html = """
    <html><body>
    <h1>Welcome to Film Explorer</h1>
    <p>Explore the best films here!</p>
    </body></html>
    """
    return HttpResponse(html)

from django.shortcuts import render
def film_list_template(request):
    films = ["Inception", "Interstellar", "The Matrix"]
    return render(request, "films02_list.html", {"films": films})

from django.shortcuts import render

def film_detail(request, title):
    return render(request, "film_detail.html", {"film_title": title})

from films.models import Film
from django.shortcuts import render

def films05_with_links(request):
    films = Film.objects.all()
    return render(request, "films04_list.html", {"films": films})

def film_detail_slug(request, slug):
    film = Film.objects.get(slug=slug)
    return render(request, "film_detail.html", {"film_title": film.title})

def films06_datatable(request):
    films = Film.objects.all()
    return render(request, "films05_list.html", {"films": films})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('films07')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def films07_view(request):
    if request.user.is_authenticated:
        return render(
            request,
            'films07_logged_in.html',
            {'username': request.user.username}
        )
    else:
        return render(request, 'films07_anonymous.html')
    
@login_required
def film_detail03(request, slug):
    film = get_object_or_404(Film2, slug=slug)

    if request.method == 'POST':
        if request.user in film.viewed_by.all():
            film.viewed_by.remove(request.user)
        else:
            film.viewed_by.add(request.user)

        return redirect('film_detail03', slug=slug)

    return render(request, 'film_detail03.html', {'film': film})