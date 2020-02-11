from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from .models import Book

class addPost(forms.Form):
    message = forms.CharField(widget=forms.TextInput, max_length=280)
    OPTIONS = (
        (True, "Boast"),
        (False, "Roast"))
    is_Boast = forms.BooleanField(
        widget=forms.CheckboxSelectMultiple(choices=OPTIONS))

    


class BookForm(BSModalForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']
