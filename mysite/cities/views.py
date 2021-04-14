# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cities.models import State, City


class CityList(LoginRequiredMixin, View):
    def get(self, request):
        sc = State.objects.all().count()
        cl = City.objects.all()
        ctx = {'state_count': sc, 'city_list': cl}
        return render(request, 'cities/city_list.html', ctx)


class StateView(LoginRequiredMixin, View):
    def get(self, request):
        sl = State.objects.all()
        ctx = {'state_list': sl}
        return render(request, 'cities/state_list.html', ctx)


class StateCreate(LoginRequiredMixin, CreateView):
    model = State
    fields = '__all__'
    success_url = reverse_lazy('cities:all')


class StateUpdate(LoginRequiredMixin, UpdateView):
    model = State
    fields = '__all__'
    success_url = reverse_lazy('cities:all')


class StateDelete(LoginRequiredMixin, DeleteView):
    model = State
    fields = '__all__'
    success_url = reverse_lazy('cities:all')

class CityCreate(LoginRequiredMixin, CreateView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('cities:all')


class CityUpdate(LoginRequiredMixin, UpdateView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('cities:all')


class CityDelete(LoginRequiredMixin, DeleteView):
    model = City
    fields = '__all__'
    success_url = reverse_lazy('cities:all')

