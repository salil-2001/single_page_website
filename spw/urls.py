from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',empl,name="empl"),
    path('delete/<int:id>/',delete1,name="delete"),
    path('login/',loginpage,name='login'),
    path('userlist/',userlist,name='userlist'),
    path('export/',export_to_csv,name='export'),
    path('import/',import_csv,name='import'),
    
]
