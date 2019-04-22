# Generated by Django 2.0.2 on 2019-04-15 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruiter',
            old_name='description',
            new_name='company_description',
        ),
        migrations.RenameField(
            model_name='recruiter',
            old_name='name',
            new_name='company_name',
        ),
        migrations.AddField(
            model_name='recruiter',
            name='company_logo',
            field=models.URLField(blank=True, null=True),
        ),
    ]
