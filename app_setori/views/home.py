from django.shortcuts import render, redirect

from django.views import View


class HomeViews(View):
    def get(self, request):
        return render(request, 'setori_view/home/index.html')
