# Generated by Django 3.2.12 on 2022-03-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djuser',
            name='userType',
            field=models.IntegerField(choices=[(1, 'client'), (2, 'Freelancer')], null=True),
        ),
    ]