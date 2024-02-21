from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("game/", views.game, name='game'),
    path("education/", views.education, name='education'),
    path("about/", views.about, name='about'),
]