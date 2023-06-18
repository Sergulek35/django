from django.urls import path
from reminders import views

app_name = 'reminders'

urlpatterns = [

    path('', views.index, name = 'index'),
    path('create/', views.create_person, name = 'create'),
    path('delete/', views.delete_person, name = 'delete'),
    path('projects/', views.change, name = 'projects')

]
