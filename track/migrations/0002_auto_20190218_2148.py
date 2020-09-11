# Generated by Django 2.1.1 on 2019-02-18 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingform',
            name='face_advocate_sv_hours',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='trackingform',
            name='hours_education',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='trackingform',
            name='hours_on_case',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='trackingform',
            name='hours_spent',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='trackingform',
            name='miles_driven',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='trackingform',
            name='supervisor',
            field=models.CharField(choices=[('C', 'Celena'), ('H', 'Heidi'), ('G', 'Gail'), ('K', 'Katie'), ('P', 'Pete'), ('M', 'Melanie'), ('N', 'Nicole')], max_length=2),
        ),
    ]