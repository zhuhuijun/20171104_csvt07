# Create your views here.
# coding:utf-8 	
from blog.models import Author
from blog.models import Book

from django.shortcuts import render_to_response


def show_author(req):
	authors = Author.objects.all()
	return render_to_response('show_author.html',{'authors':authors})

def show_book(req):
	books = Book.objects.all()
	return render_to_response('show_book.html',{'books',books})