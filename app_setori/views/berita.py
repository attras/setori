from django.shortcuts import render, redirect

from django.views import View


class BeritaViews(View):
    def get(self, request):
        return render(request, 'setori_view/berita/index.html')