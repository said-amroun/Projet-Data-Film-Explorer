from django.contrib import admin
from django.urls import path
from films.views import (
    film_list,
    film_list_template,
    film_detail,
    films04_db,
    films05_with_links,
    film_detail_slug,
)
from films.views import films06_datatable
from films import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('films01/', film_list, name='film_list'),
    path('films02/', film_list_template, name='film_list_template'),

    path('film_detail01/<str:title>/', film_detail, name='film_detail'),

    path('films04/', films04_db, name='films04_db'),
    path('films05/', films05_with_links, name='films05_with_links'),

    path('film/<slug:slug>/', film_detail_slug, name='film_detail_slug'),

    path('films06/', films06_datatable, name='films06_datatable'),

    path('signup/', views.signup, name='signup'),

    path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='registration/login.html',
        next_page='films07'
    ),
    name='login'
    ),

    path('films07/', views.films07_view, name='films07'),

    path(
    'film_detail03/<slug:slug>/',
    views.film_detail03,
    name='film_detail03'),

    path(
    'search/',
    views.film_search,
    name='film_search'),
]