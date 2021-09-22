from django.urls import path
from .import views

urlpatterns = [
    # обращаемся к методам views, для отслеживания url адресов в отношении фильмы
    path('', views.cinema_home, name='cinema_home'),
    path('create_films', views.create, name='create_films'),
    path('<int:pk>/', views.FilmsDetailView.as_view(), name='films-detail'),
    path('<int:pk>/update', views.FilmsUpdateView.as_view(), name='films-update'),
    path('<int:pk>/delete', views.FilmsDeleteView.as_view(), name='films-delete'),

    # обращаемся к методам views, для отслеживания url адресов в отношении актеры
    path('actors', views.actors, name='actors'),
    path('create_actors', views.create_actors, name='create_actors'),
    path('create_contacts', views.create_contacts, name='create_contacts'),

    # обращаемся к методам views, для отслеживания url адресов в отношении работники
    path('workers', views.workers, name='workers'),
    path('create_workers', views.create_workers, name='create_workers'),
]
