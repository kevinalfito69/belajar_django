# Generated by Django 4.0 on 2021-12-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50, verbose_name='Judul')),
                ('body', models.TextField(verbose_name='Body Postingan')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('category', models.CharField(choices=[('Jurnal', 'jurnal'), ('Berita', 'berita'), ('Gosip', 'gosip')], max_length=50, verbose_name='Category')),
            ],
        ),
    ]