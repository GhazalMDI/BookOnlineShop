from django.shortcuts import render
from django.views import View
from Home.models import Banner
from Book.models import Book


class HomeView(View):
    TEMPLATE_NAME = 'home/home.html'

    def get(self, request):
        try:
            books = Book.objects.all()
            new_books = books.order_by('-created')[:10]
            if banners := Banner.objects.all():
                ctx = {
                    'books':new_books
                    'banners': banners
                }
                return render(request, self.TEMPLATE_NAME, ctx)

        except:
            return render(request, self.TEMPLATE_NAME)
