# Generated by Django 3.2.9 on 2022-03-08 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_office_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]