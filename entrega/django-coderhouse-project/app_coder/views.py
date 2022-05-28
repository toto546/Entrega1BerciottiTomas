from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from app_coder.models import Copas, Clubes, Ligas
from app_coder.forms import  CopasForm, ClubesForm, LigasForm


def index(request):
    return render(request, "app_coder/home.html")

# -----------------------Todo lo relacionado al model Clubes----------------
def clubes(request):
    clubes = Clubes.objects.all()

    context_dict = {
        'clubes': clubes
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/clubes.html"
    )

def form_clubes(request):
    if request.method == 'POST':
        clubes_form = ClubesForm(request.POST)
        
        if clubes_form.is_valid():
            data = clubes_form.cleaned_data
            club = Clubes(
                name=data['name'],
                division=data['division'],
                liga=data['liga'],
            )
            club.save()
            

            clubes = Clubes.objects.all()
            context_dict = {
                'clubes': clubes
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/clubes.html"
            )
          

    clubes_form = ClubesForm(request.POST)
    context_dict = {
        'clubes_form': clubes_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/formCLUB.html'
    )
# ----------------------------------------------------------------------------- 


#---------------------------Todo lo relacionado al model Ligas-----------------
def ligas(request):
    ligas = Ligas.objects.all()

    context_dict = {
        'ligas': ligas
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/ligas.html"
    )


def form_ligas(request):
    if request.method == 'POST':
        ligas_form = LigasForm(request.POST)
        
        if ligas_form.is_valid():
            data = ligas_form.cleaned_data
            liga = Ligas(
                name=data['name'],
                pais=data['pais'],
            )
            liga.save()
            

            ligas = Ligas.objects.all()
            context_dict = {
                'ligas': ligas
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/ligas.html"
            )
          

    ligas_form = LigasForm(request.POST)
    context_dict = {
        'ligas_form': ligas_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/ligasFORM.html")
#-----------------------------------------------------------------------------



#----------------------Todo lo relacionado al model Copas---------------------
def copas(request):
    copas = Copas.objects.all()

    context_dict = {
        'copas': copas
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/copas.html"
    )

def form_copas(request):
    if request.method == 'POST':
        print("TEST##############") 
        copas_form = CopasForm(request.POST)
        
        if copas_form.is_valid():
            data = copas_form.cleaned_data
            copa = Copas(
                name=data['name'],
                pais=data['pais'],
            )
            copa.save()
            print("TEST##############")

            copas = Copas.objects.all()
            context_dict = {
                'copas': copas
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/copas.html"
            )
          

    copas_form = CopasForm(request.POST)
    context_dict = {
        'copas_form': copas_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/formCOPAS.html'
    )



#----------------------------Buscador-----------------------------------------
def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        clubes = Clubes.objects.filter(name__contains=search_param)
        context_dict = {
            'clubes': clubes
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )

