from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    #path('article/<int:id_article>', views.view_article),
    #path('articles/<str:tag>', views.list_articles_by_tag),
    #path('articles/<int:year>/<int:month>', views.list_articles),
    path('redirection', views.view_redirection),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('', views.accueil, name='accueil'),
    #path('article/<int:id>', views.lire, name='lire'),
    path('article/<int:id>-<slug:slug>$', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
    path('nouveau_contact/', views.nouveau_contact, name='nouveau_contact'),
    path('voir_contacts/', views.voir_contacts),
    url(r'^connexion$', views.connexion, name='connexion'),
    url(r'^deconnexion$', views.deconnexion, name='deconnexion'),
]

