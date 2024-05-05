from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('add/',views.add_task, name='add_task'),
    path('show/',views.show_task, name='show_task'),
    path('edit/<int:id>',views.edit_task, name='edit_task'),
    path('delete/<int:id>',views.delete_task, name='delete_task'),
]
