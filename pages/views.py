from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class HomePageView(View):
	def get(self, request):
		messages.success(request, "Homepage")
		return render(request, 'pages/home.html')


class DashboardView(LoginRequiredMixin, View):
	def get(self, request):
		return render(request, 'pages/dashboard.html')