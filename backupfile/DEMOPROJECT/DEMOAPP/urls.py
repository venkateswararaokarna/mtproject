from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi,name = 'homepage'),
    path('webhooks',views.webhooks,name='webhooks'),
    path('sentmessages',views.sentmessages,name='sentmessages')
]
