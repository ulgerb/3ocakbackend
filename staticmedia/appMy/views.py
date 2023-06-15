from django.shortcuts import render
from .models import *

# request = istek (sayfa içerisindeki bilgileri alıp geri döndürür)
def indexPage(request):

   # bu yazının içinde kaç i harfi vardır
   text = "bugün django değişkenleri öğreniyoruz"
   i = text.count("i")
   context = {
      "text": "naberrr",
      "i":i,
      "asd":1000,
   }
   return render(request,'index.html',context)

def aboutPage(request):
   return render(request,'about.html', {"başlık":"Django"})

def bookPage(request):
   books = Book.objects.all()
   context = {
      "books":books,
   }
   return render(request, 'books.html', context)


