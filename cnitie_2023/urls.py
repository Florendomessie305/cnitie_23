"""
URL configuration for cnitie_2023 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import newsletter.urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from cnitie_2023.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsletter/', include('newsletter.urls')),
    path('', home_page, name='home'),

    # activité link
    path('home/atelier-sensibilisation/', atelierSensibilisation, name='atelier-sensibilisation'),
    path('home/atelier-vulgarisation/', atelierVulgarisation, name='atelier-vulgarisation'),
    path('home/meeting-report/', meetingReport, name='meeting-report'),

    # contact link
    path('home/secteurMinier/', secteurMinier, name='secteurMinier'),
    path('home/secteurForestier/', secteurForestier, name='secteurForestier'),
    path('home/secteurHydrocarbure/', secteurHydrocarbure, name='secteurHydrocarbure'),

    # ropport link
    path('home/rapportItie/', rapportSuivi, name='rapportItie'),
    path('home/revenusVentePetrolier/', revenusVentePetrolier, name='revenusVentePetrolier'),
    path('home/rapportActivite/', rapportActivite, name='rapportActivite'),

    # publication link
    path('home/universite/', universite, name='universite'),
    path('home/loi/', loi, name='loi'),
    path('home/resultat/', resultat, name='resultat'),

    # validation link
    path('home/note/', note, name='note'),
    path('home/administration/', administration, name='administration'),
    path('home/ministere/', ministere, name='ministere'),

    # a propos
    path('home/mission/', mission, name='mission'),
    path('home/gouvernance/', gouvernance, name='gouvernance'),
    path('home/historique/', historique, name='historique'),
    path('home/texte/', texte, name='texte'),

    # prodiction-commercialisation url
    path('home/production/', production, name='production'),
    path('home/commercialisation/', commercialisation, name='commercialisation'),

    # propriétés réelles url
    path('home/propriete/', Propriete, name='propriete'),

    # licences_registre url
    path("home/licences", licences_registre, name='licences'),

    # blog urls
    path("blog/", include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

