from django.conf.urls import url
from . import views

urlpatterns = [
    # Une string vide indique la racine
    url(r'^$', views.liste, name='url_liste'),
    url(r'^nouveau$', views.nouveau, name='url_nouveau'),
    # (?P<code>\w{6}) capturera 6 caractères alphanumériques.
    url(r'^(?P<code>\w{6})/$', views.redirection, name='url_redirection'),
]