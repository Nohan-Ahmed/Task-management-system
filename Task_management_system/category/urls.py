from django.urls import path
from . import views

app_name = 'category'
urlpatterns = [
    path('add/',views.add_category, name='add_category')
]
