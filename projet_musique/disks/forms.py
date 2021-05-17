from django import forms


class RechercheForm(forms.Form):
    recherche = forms.CharField(max_length=200)