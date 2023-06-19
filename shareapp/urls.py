from django.urls import path
from . import views

urlpatterns = [
    path('notes/<int:note_id>/share/', views.share_note, name='share_note'),
    path('login/', views.login_view, name='login'),
    path('index',views.index,name='dashboard'),
     path('notes/', views.display_notes, name='display_notes'),
     path('register/', views.register, name='register'),
]
