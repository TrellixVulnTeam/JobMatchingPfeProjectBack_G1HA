# Generated by Django 2.0.2 on 2019-06-10 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='company_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]