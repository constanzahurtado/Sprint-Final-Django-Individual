# Generated by Django 3.2.9 on 2021-12-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora_nutricional', '0021_auto_20211209_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=2)),
                ('street', models.CharField(max_length=100)),
            ],
        ),
    ]
