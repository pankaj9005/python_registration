from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('home/',home),
    path('add-std/',std_add),
    path('delete-std/<int:age>',delete_std),
    path('update-std/<int:age>',update_std),
    path('do-update-std/<int:age>',do_update_std),
    path('view-std/<int:age>',view_std),
]