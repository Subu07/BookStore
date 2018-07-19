from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from . import views
from .views import CreateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'users', CreateView)
urlpatterns = [

    path('', views.home, name='index'),

    path('booklist/', CreateView.as_view(), name='create')

]
