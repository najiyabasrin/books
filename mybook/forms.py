from dataclasses import fields
from socket import fromshare
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from mybook.models import Books
class BookForm(forms.Form):
    bookname=forms.CharField(required=True)
    author=forms.CharField(required=True)
    price=forms.IntegerField(required=True)



class BookModelForm(forms.ModelForm):
    class Meta:
        model=Books
        fields="__all__"

        widgets={
        "bookname":forms.TextInput(attrs={"class":"form-control"}),
        "author":forms.TextInput(attrs={"class":"form-control"}),
        "price":forms.TextInput(attrs={"class":"form-control"})


    }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
