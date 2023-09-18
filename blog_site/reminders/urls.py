from django.urls import path
from reminders import views

app_name = 'reminders'

urlpatterns = [

    path('radmi-delete/<int:pk>/', views.RadmiDeleteView.as_view(), name = 'radmi_delete'),
    path('radmi-list/', views.RadmiListView.as_view(), name='radmi_list'),
    path('radmi-create/', views.RadmiCreateView.as_view(), name='radmi_create'),
    path('radmi-update/<int:pk>/', views.RadmiUpdataView.as_view(), name='radmi_update'),
    path('messages-create/', views.MessagCreateView.as_view(), name='messages_create'),
    path('messages/', views.MessagListView.as_view(), name='messages'),
    path('messages-delete/<int:pk>/', views.MessagDeleteView.as_view(), name='messages_delete'),
    path('messages-update/<int:pk>/', views.MessagUpdataView.as_view(), name='messages_update'),

    path('index/', views.RadmiIndexView.as_view(), name = 'index'),

]
