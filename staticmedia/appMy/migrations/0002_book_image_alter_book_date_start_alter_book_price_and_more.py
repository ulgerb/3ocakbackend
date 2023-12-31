# Generated by Django 4.1.5 on 2023-06-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.FileField(null=True, upload_to='', verbose_name='Resim'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_start',
            field=models.DateField(verbose_name='Basın Tarihi'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
    ]
