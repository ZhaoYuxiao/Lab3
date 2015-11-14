#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
import time
import datetime
from django.db.models import Q
from django.db import connection
from django import template
import os 
from books.models import Book,Author

def search(request):
    error = False
    authors = Author.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        try:
            author = Author.objects.get(name__contains=q)
        except Author.DoesNotExist:
            error = True
            return render_to_response('search_forms.html',{'authors':authors,'error': error})
        else:
            ids=author.authorid
            books = Book.objects.filter(authorid_id=ids)
            return render_to_response('search_results.html',{'author':author,'books': books, 'query': q})
    return render_to_response('search_form.html',{'error': error})
    
def index(request):
    authors = Author.objects.all()
    return render_to_response('search_form.html',{'authors':authors})

def zhanshi(request,book_id):
    book = Book.objects.get(isbn=book_id)
    aid = book.authorid_id
    author = Author.objects.get(authorid=aid)
    return render_to_response('xiangxi.html',{'author':author,'book': book})

def dele(request,book_id,au_id):
    book = Book.objects.get(isbn=book_id)
    book.delete()
    author = Author.objects.get(authorid=au_id)
    books = Book.objects.filter(authorid_id=au_id)
    return render_to_response('zhanshiauthor.html',{'author':author,'books': books})
    
def update(request,book_id,au_id):
    errors = []
    book = Book.objects.get(isbn=book_id)
    auth = Author.objects.get(authorid = au_id)

    books = Book.objects.filter(authorid_id=au_id)
    if 'author' in request.GET:
        author = request.GET['author']
        try:   
            Au = Author.objects.get(name=author)
        except Author.DoesNotExist:
            errors.append('您输入的作者不存在')
            publisher = request.GET['publisher']
            publishDate = request.GET['publishDate']
            price = request.GET['price']
            book = Book.objects.get(isbn=book_id)
            book.publisher = publisher
            book.publishDate = str(publishDate)
            book.price = price
            book.save()
            return render_to_response('appauthor.html', {'book_id': book_id})
        else:
            authorid = Au.authorid
            publisher = request.GET['publisher']
            publishDate = request.GET['publishDate']
            price = request.GET['price']
            book = Book.objects.get(isbn=book_id)
            book.authorid_id = authorid
            book.publisher = publisher
            book.publishDate = publishDate
            book.price = price
            book.save()
            return render_to_response('zhanshiauthor.html',{'author':auth, 'books': books})       
    return render_to_response('update.html',{'auth':auth, 'book': book})
    
def append(request):
    errors = []
    if 'isbn' in request.GET:
        ISBN = request.GET['isbn']
        try:   
            book = Book.objects.get(isbn=ISBN)
        except Book.DoesNotExist:
            name = request.GET['name']
            try:
                Au = Author.objects.get(name=name)
            except Author.DoesNotExist:
#作者不存在则添加作者
                title = request.GET['title']
                publisher = request.GET['publisher']
                publishDate = request.GET['publishDate']
                price = request.GET['price']
                p1 = Book(isbn=ISBN, title=title, authorid_id=1, publisher=publisher,
                          publishDate=str(publishDate), price=price )
                p1.save()
                return render_to_response('appauthor.html',{'book_id': ISBN})    
            else:
                authorid = Au.authorid
                title = request.GET['title']
                publisher = request.GET['publisher']
                publishDate = request.GET['publishDate']
                price = request.GET['price']
                p1 = Book(isbn=ISBN, title=title, authorid_id=authorid, publisher=publisher,
                          publishDate=publishDate, price=price )
                p1.save()
                return render_to_response('appendsuccess.html')     
        else:
            errors.append('输入的ISBN已经存在')
            render_to_response('append.html', {'errors': errors})
    return render_to_response('append.html',{'errors': errors})

def appauthor(request,book_id):
    errors = []
    bid = book_id
    if 'name' in request.GET:
        name = request.GET['name']
        try:
            author = Author.objects.get(name = name)
        except Author.DoesNotExist:
            Au = Author.objects.all()
            tmp = Au[0].authorid
            for i in range(1,len(Au)):
                if Au[i].authorid>tmp:
                    tmp=Au[i].authorid
            for j in range(tmp):
                aid = j+1
                try:
                    per=Author.objects.get(authorid=aid)
                except Author.DoesNotExist:
                    break
            authorid = aid
            age = request.GET['age']
            country = request.GET['country']
            p1 = Author(authorid=authorid, name=name, age=age, country=country)
            p1.save()
            
            book = Book.objects.get(isbn=bid)
            book.authorid_id = authorid
            book.save()
            return render_to_response('appendsuccess.html')  
        else:
            errors.append('输入的作者在作者库中已经存在')
            render_to_response('appauthor.html', {'book_id': bid,'errors': errors})
    return render_to_response('appauthor.html',{'book_id': bid,'errors': errors})

# Create your views here.
# Create your views here.
