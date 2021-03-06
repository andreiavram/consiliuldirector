# Generated by Django 2.0.6 on 2019-01-16 01:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiuneDecizie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentariu', models.TextField(blank=True, null=True)),
                ('fisier', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('fisier_link', models.URLField(blank=True, null=True)),
                ('sursa', models.CharField(blank=True, max_length=255, null=True)),
                ('vot', models.IntegerField(blank=True, choices=[(1, 'Pentru'), (2, 'Împotrivă'), (3, 'Abținere'), (4, 'Absență')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConsiliulDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mandat_inceput', models.IntegerField()),
                ('mandat_sfarsit', models.IntegerField()),
                ('index', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Decizie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numar', models.IntegerField(unique=True)),
                ('titlu', models.CharField(max_length=1024)),
                ('text', models.TextField(null=True)),
                ('deadline_vot', models.DateTimeField(blank=True, null=True)),
                ('data_creata', models.DateTimeField(auto_now_add=True)),
                ('vot_presupus', models.IntegerField(blank=True, choices=[(1, 'Draft'), (2, 'Propunere'), (3, 'Vot deschis'), (4, 'Vot finalizat'), (5, 'Propunere retrasă')], null=True)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Propunere'), (3, 'Vot deschis'), (4, 'Vot finalizat'), (5, 'Propunere retrasă')])),
            ],
        ),
        migrations.CreateModel(
            name='IntrareRegistru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numar', models.IntegerField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MembruConsiliulDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('functie', models.CharField(blank=True, max_length=255, null=True)),
                ('poza_profil', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('consiliu_director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decizii.ConsiliulDirector')),
                ('membru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=255)),
                ('next_number', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='intrareregistru',
            name='registru',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decizii.Registru'),
        ),
        migrations.AddField(
            model_name='decizie',
            name='initiator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='decizii.MembruConsiliulDirector'),
        ),
        migrations.AddField(
            model_name='actiunedecizie',
            name='decizie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decizii.Decizie'),
        ),
        migrations.AddField(
            model_name='actiunedecizie',
            name='membru',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decizii.MembruConsiliulDirector'),
        ),
    ]
