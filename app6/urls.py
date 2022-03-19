from app6.views import app6
from django.urls import path
app_name='app6'
urlpatterns=[
    path('app6/',app6,name='app6')
]
