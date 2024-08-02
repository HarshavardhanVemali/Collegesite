from django.contrib import admin
from django.urls import path
from collegesiteapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('testpage/',views.testpage,name='testpage'),
    path('aboutcollege/',views.aboutcollege,name='aboutcollege'),
    path('aboutset/',views.aboutset,name='aboutset'),
    path('aboutconference/',views.aboutconference,name='aboutconference'),
    path('keytonespeakers/',views.keytonespeakers,name='keytonespeakers'),
    path('registation/',views.registration,name='registration'),
    path('callforpapers/',views.callforpapers,name='callforpapers'),
    path('submitpapers/',views.submitpaper,name='submitpapers'),
    path('publication/',views.publication,name='publication'),
    path('venue/',views.venue,name='venue'),

]
