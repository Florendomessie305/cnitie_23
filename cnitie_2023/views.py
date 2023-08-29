from django.shortcuts import render


def home_page(request):
    return render(request, 'pages/home_page.html', {})


# activité views
def atelierSensibilisation(request):
    return render(request, 'pages/activites/atelier_sensibilisation.html', {})


def atelierVulgarisation(request):
    return render(request, 'pages/activites/atelier_vulgarisation.html', {})


def meetingReport(request):
    return render(request, 'pages/activites/compte-rendu-sessions.html', {})


# contact views
def secteurMinier(request):
    return render(request, 'pages/contrats/secteur-minier.html', {})


def secteurForestier(request):
    return render(request, 'pages/contrats/secteur-forestier.html', {})


def secteurHydrocarbure(request):
    return render(request, 'pages/contrats/secteur-hydrocarbure.html', {})


# rapport views
def rapportSuivi(request):
    return render(request, 'pages/rapports/rapport-itie.html', {})


def revenusVentePetrolier(request):
    return render(request, 'pages/rapports/revenus-ventes.html', {})


def rapportActivite(request):
    return render(request, 'pages/rapports/rapport-activites.html', {})


# publication views
def universite(request):
    return render(request, 'pages/publications/umn.html', {})


def loi(request):
    return render(request, 'pages/publications/lois.html', {})


def resultat(request):
    return render(request, 'pages/publications/resultat.html', {})


# validation views
def note(request):
    return render(request, 'pages/validations/note-et-memoire.html', {})


def administration(request):
    return render(request, 'pages/validations/administrateur-independant.html', {})


def ministere(request):
    return render(request, 'pages/validations/mfbpp.html', {})


# a propos
def mission(request):
    return render(request, 'pages/a_propos/missions.html', {})


def gouvernance(request):
    return render(request, 'pages/a_propos/gouvernance.html', {})


def historique(request):
    return render(request, 'pages/a_propos/historique.html', {})


def texte(request):
    return render(request, 'pages/a_propos/textes.html', {})


# prodiction-commercialisation views
def production(request):
    return render(request, 'pages/production_com/production.html', {})


def commercialisation(request):
    return render(request, 'pages/production_com/commercialisation.html', {})


# propriétés réeles views
def Propriete(request):
    return render(request, 'pages/propriete_r/proprietes-reel.html', {})


# licence views
def licences_registre(request):
    return render(request, 'pages/licences_registre.html', {})

