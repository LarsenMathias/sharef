from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('index',views.index,name='dashboard'),
     path('notes/', views.display_notes, name='display_notes'),
     path('register/', views.register, name='register'),
]
