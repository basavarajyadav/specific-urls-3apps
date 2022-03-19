from app4.views import app4
from django.urls import path
app_name='app4'
urlpatterns=[
    path('app4/',app4,name='app4')
]