# Generated by Django 4.2.4 on 2023-11-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sasvar_app', '0005_alter_waste_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='waste',
            name='model_version',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='waste',
            name='container_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='waste',
            name='waste_type',
            field=models.CharField(max_length=50),
        ),
    ]
