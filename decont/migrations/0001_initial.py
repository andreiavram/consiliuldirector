# Generated by Django 2.0.6 on 2019-03-03 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decont',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.CharField(help_text='Nume și prenume', max_length=255)),
                ('activitatea', models.CharField(max_length=1024)),
                ('centrul_local', models.CharField(blank=True, max_length=1024, null=True)),
                ('perioada_start', models.DateField()),
                ('perioada_stop', models.DateField()),
                ('data_decont', models.DateTimeField()),
                ('valuta', models.CharField(choices=[(1, 'RON'), (2, 'EUR'), (3, 'USD'), (4, 'HUF')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='LinieAvans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_plata', models.CharField(help_text='Felul și numărul documentului de plată', max_length=255)),
                ('data', models.DateField()),
                ('valoarea', models.FloatField()),
                ('decont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decont.Decont')),
            ],
        ),
        migrations.CreateModel(
            name='LinieDecont',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('descriere_cheltuieli', models.CharField(help_text='Descriere cheltuieli', max_length=1024)),
                ('furnizor', models.CharField(max_length=255)),
                ('tip_document', models.IntegerField(choices=[(1, 'Bon Fiscal'), (2, 'Chitanță'), (3, 'Bilet intrare'), (4, 'Bilet transport'), (5, 'Tichet')])),
                ('numar_document', models.CharField(max_length=255)),
                ('data_document', models.DateField()),
                ('valoare', models.FloatField()),
                ('decont', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decont.Decont')),
            ],
        ),
    ]
