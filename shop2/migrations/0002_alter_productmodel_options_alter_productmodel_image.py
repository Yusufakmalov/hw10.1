# Generated by Django 4.2.6 on 2023-10-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop2', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodel',
            options={'verbose_name': 'shop', 'verbose_name_plural': 'shop2'},
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.FileField(upload_to='shop2'),
        ),
    ]
