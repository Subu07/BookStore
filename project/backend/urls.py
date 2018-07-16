from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from . import views
from .views import CreateView

router = routers.DefaultRouter()
router.register(r'users', CreateView)
urlpatterns = [

    path('', views.index, name='index'),
    path('booklist/', CreateView.as_view(), name='create')

]
