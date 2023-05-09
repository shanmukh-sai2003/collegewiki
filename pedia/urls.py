from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("login/", views.login_view, name = "login"),
    path("<str:name>/", views.fullPage, name = "fullPage"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name = 'signup'),
    path('add/', views.add, name = "add"),
]

