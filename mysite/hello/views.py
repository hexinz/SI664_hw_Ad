# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# import logging

def cookie(request):
    print(request.COOKIES)
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('dj4e_cookie', 'ada9e980', max_age=1000) # seconds until expire
    return resp

