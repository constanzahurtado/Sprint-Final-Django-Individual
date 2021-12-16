# Generated by Django 3.2.9 on 2021-12-08 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora_nutricional', '0010_collection_collectiontitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ingrediente', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_receta', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='collectiontitle',
            name='collection',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.DeleteModel(
            name='CollectionTitle',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculadora_nutricional.receta'),
        ),
    ]
