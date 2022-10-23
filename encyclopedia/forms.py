from enum import unique
from tkinter import Widget
from django import forms

class NewSearchForm(forms.Form):
    search = forms.CharField(label="Search", required=False, widget=forms.TextInput 
    (attrs={'placeholder': 'Search Encyclopedia'}))


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title", required=True, widget=forms.TextInput
    (attrs={'placeholder' : 'Title of Page'}))

    content = forms.CharField(label="Content", required=True, widget=forms.TextInput
    (attrs={'placeholder' : 'Body of Page'}))


class EditEntryForm(forms.Form):
    content = forms.CharField(label="Edit", required=True, widget=forms.TextInput
    (attrs={'placeholder':'Enter Page Content using Github Markdown'}))