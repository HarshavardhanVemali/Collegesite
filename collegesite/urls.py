from django.contrib import admin
from django.urls import path
from collegesiteapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('testpage/',views.testpage,name='testpage'),

]
