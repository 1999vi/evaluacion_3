# Generated by Django 3.2.4 on 2021-07-07 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_obra_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
