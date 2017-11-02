from django.shortcuts import render
from logNote.models import User,Log
from django.template.context_processors import csrf
import logNote.functions_DB as functions
import sys
from flask import (
    Flask, render_template,
    redirect, request,
    flash, session,
    jsonify
)


def welcome(request):
    return render(request, 'welcome.html')

def goToNote(request):
    return render(request, 'addNote.html')

def goToView(request):
    return render(request, 'search.html')
    
def home(request):
    return render(request,'home.html')


def welcomeLog(request):
    if request.method == 'POST':
        emailAd = request.POST['emailAd']
        password = request.POST['password']
        if functions.check_user(emailAd):
            return render(request,'home.html', {'password': password, 'email':emailAd})
        else:
            #I should use flash to display a message
            return render(request, 'welcome.html')
    return render(request, 'welcome.html')


def welcomeSign(request):
    if request.method == 'POST':
        emailAd = request.POST['emailAd']
        password = request.POST['password']
        firstName = request.POST['firstName']
        secondName = request.POST['secondName']
        if functions.check_user(emailAd):
            return render(request,'welcome.html')
        else:
            u = User(email = emailAd, password = password, firstName = firstName, lastName = secondName)
            u.save()
            n = User.objects.get(email = emailAd).id;
            #session['email'] = n;
            #print (session['email'])
            return render(request,'home.html', {'password': password, 'email':emailAd, 'firstName': firstName,'secondName': secondName})
    return render(request, 'welcome.html')

def makeNote(request):
    if request.method == 'POST':
        title = request.POST['noteTitle']
        currentDate = request.POST['myDate']
        currentMessage = request.POST['myNote']
        note = Log(title= title, date = currentDate, body = currentMessage, userId = session['email'])
        return render(request, 'home.html', {'title':title, 'currentDate':currentDate, 'currentMessage':currentMessage})
    return render(request, 'addNote.html')