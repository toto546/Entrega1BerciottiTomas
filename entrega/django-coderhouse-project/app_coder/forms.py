from __future__ import division
import datetime
from django import forms
from django.forms import ModelForm
from app_coder.models import Profesor



class CopasForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre de la copa')
    pais = forms.CharField(label='Pais de la copa')


class ClubesForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre de la copa')
    division = forms.CharField(label='Division')
    liga = forms.CharField(label='Liga')
    
class LigasForm(forms.Form):
    name = forms.CharField(max_length=40, min_length=3, label='Nombre de la liga')
    pais = forms.CharField(label='Pais')
    