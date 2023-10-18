from django import forms

class RecipesForm(forms.Form):
    title = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField()
    image = forms.ImageField()


    