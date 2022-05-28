from django.urls import path
from app_coder import views
from app_coder.views import form_copas, form_ligas

app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Home'),
    path('clubes', views.clubes, name='Clubes'),
    path('ligas', views.ligas, name='Ligas'),
    path('copas', views.copas, name='Copas'),
    path("formcopas", form_copas, name="formCOPAS"),
    path('formCLUB', views.form_clubes, name='formCLUB'),
    path('search', views.search, name='Search'),
    path("ligasform", form_ligas, name="ligasFORM")

]
