from rest_framework import routers
from django.urls import include, path
from rest_framework import routers
# from .api import *
from .yasg import urlpatterns as url_doc

router = routers.DefaultRouter()

urlpatterns = [
   path('accounts/', include('rest_registration.api.urls')),
] 

urlpatterns += url_doc