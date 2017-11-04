# Create your views here.
# coding:utf-8 	
from blog.models import Author,Book
from django.shortcuts import render_to_responde


def show_author(req):
	authors = Author.objects.all()
	return render_to_responde('show_author.html',{'authors':authors})