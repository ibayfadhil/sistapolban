# Generated by Django 2.2.12 on 2020-05-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perpustakaan', '0002_delete_buku'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('penulis', models.CharField(max_length=40)),
                ('penerbit', models.CharField(max_length=40)),
                ('jumlah', models.IntegerField()),
            ],
        ),
    ]
