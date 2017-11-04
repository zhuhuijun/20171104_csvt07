# Create your views here.
# coding:utf-8 	
from blog.models import Author
from blog.models import Book
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response

class UserForm(forms.Form):
	name = forms.CharField()

def show_author(req):
	authors = Author.objects.all()
	return render_to_response('show_author.html',{'authors':authors})

def show_book(req):
	books = Book.objects.all()
	return render_to_response('show_book.html',{'books',books})

def register(req):
	if req.method == 'POST':
		form = UserForm(req.POST)
		if form.is_valid():
			print form.cleand_data
			return HttpResponse('ok')
	else:
		form = UserForm()
	return render_to_response('register.html',{'form':form})