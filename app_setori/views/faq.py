from django.shortcuts import render, redirect

from django.views import View


class FaqViews(View):
    def get(self, request):
        return render(request, 'setori_view/faq/index.html')