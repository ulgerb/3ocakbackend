from django.db import models

# py manage.py migrate
# py manage.py createsuperuser


class Book(models.Model):
   title = models.CharField(verbose_name="Başlık", max_length=50) # input text
   date_start = models.DateField(("Basın Tarihi"), auto_now_add=False) # input date
   text = models.TextField(("Konusu")) # textarea
   price = models.FloatField(("Fiyat")) # input number
   image = models.FileField(("Resim"), upload_to="", max_length=100, null=True)

   def __str__(self):
      return self.title