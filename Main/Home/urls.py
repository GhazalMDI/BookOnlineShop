from django.urls import include, path
from Home import views

app_name = 'Home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
