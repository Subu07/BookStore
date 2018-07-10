from  django.conf.urls import url,include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
router = routers.DefaultRouter()
router.register(r'users', CreateView)
urlpatterns = [
    url(r'^booklist/$', CreateView.as_view(), name='create')

]

urlpatterns = format_suffix_patterns(urlpatterns)