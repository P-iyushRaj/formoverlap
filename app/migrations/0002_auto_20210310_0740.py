# Generated by Django 3.0.1 on 2021-03-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dob_day',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dob_month',
            field=models.IntegerField(choices=[('1', 'january'), ('2', 'february'), ('3', 'march'), ('4', 'april')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dob_year',
            field=models.IntegerField(choices=[('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995')]),
        ),
    ]
