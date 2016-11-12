from django.conf.urls import url
from . import views

app_name = "hanging"
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^game$', views.game, name = 'game'),
    url(r'^loop$', views.loop, name = 'loop'),
]
