from django.shortcuts import render
from django.views import View


class HomeView(View):
    TEMPLATE_NAME = 'home/home.html'

    def get(self, request):
        return render(request, self.TEMPLATE_NAME)
