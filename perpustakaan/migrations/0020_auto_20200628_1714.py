# Generated by Django 2.2.12 on 2020-06-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0019_auto_20200628_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
        migrations.AddField(
            model_name='buku',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]