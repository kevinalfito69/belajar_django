# Generated by Django 4.0 on 2021-12-21 15:33

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
                ('nama', models.CharField(max_length=40)),
                ('jenis_kelamin', models.CharField(choices=[('Laki-Laki', 'laki-laki'), ('Perempuan', 'perempuan')], max_length=40)),
                ('alamat', models.TextField()),
                ('tanggal_lahir', models.DateTimeField()),
            ],
        ),
    ]
