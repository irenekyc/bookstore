# Generated by Django 3.2.3 on 2021-06-02 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]