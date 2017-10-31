from django.shortcuts import render
from logNote.models import User,Log
from django.template.context_processors import csrf
import sys
from flask import (
    Flask, render_template,
    redirect, request,
    flash, session,
    jsonify
)


def welcome(request):
    return render(request, 'welcome.html')


def home(request):
    return render(request,'home.html')


def welcomeLog(request):
    if request.method == 'POST':
        emailAd = request.POST['emailAd']
        password = request.POST['password']
    return render(request,'home.html', {'password': password, 'email':emailAd})


def welcomeSign(request):
    if request.method == 'POST':
        emailAd = request.POST['emailAd']
        password = request.POST['password']
        firstName = request.POST['firstName']
        secondName = request.POST['secondName']
    #check if the email does not exist and save in the db
    u = User(email = emailAd, password = password, firstName = firstName, lastName = secondName)
    u.save();
    return render(request,'home.html', {'password': password, 'email':emailAd, 'firstName': firstName,'secondName': secondName})