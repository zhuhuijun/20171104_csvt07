# Create your views here.
# coding:utf-8 	
from blog.models import Author
from blog.models import Book
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response

class UserForm(forms.Form):
	name = forms.CharField()
	headImg = forms.FileField()

def show_author(req):
	authors = Author.objects.all()
	return render_to_response('show_author.html',{'authors':authors})

def show_book(req):
	books = Book.objects.all()
	return render_to_response('show_book.html',{'books',books})

def register(req):
	if req.method == 'POST':
		form = UserForm(req.POST,req.FILES)
		if form.is_valid():
			print form.cleaned_data
			print req.FILES
			print form.cleaned_data['headImg']
			print form.cleaned_data['headImg'].name
			print form.cleaned_data['headImg'].size
			fp = file('/uploadfile/'+form.cleaned_data['headImg'].name,'wb')
			return HttpResponse('ok')
	else:
		form = UserForm()
	return render_to_response('register.html',{'form':form})