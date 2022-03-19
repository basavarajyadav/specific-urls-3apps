from app5.views import app5
from django.urls import path
app_name='app5'
urlpatterns=[
    path('app5/',app5,name='app5')
]