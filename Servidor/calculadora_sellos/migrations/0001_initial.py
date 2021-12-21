# Generated by Django 3.2.9 on 2021-12-21 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('mensaje', models.TextField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=12)),
                ('nombre_grupo_usuario', models.CharField(choices=[('Usuario', 'Usuario'), ('Administrador', 'Administrador')], max_length=20)),
                ('last_login', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_receta', models.CharField(max_length=30)),
                ('porcion', models.FloatField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ingrediente', models.CharField(max_length=30)),
                ('cantidad', models.FloatField()),
                ('calorias', models.FloatField()),
                ('azucares', models.FloatField()),
                ('sodio', models.FloatField()),
                ('grasas', models.FloatField()),
                ('totalCalorias', models.FloatField()),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculadora_sellos.receta')),
            ],
        ),
    ]
