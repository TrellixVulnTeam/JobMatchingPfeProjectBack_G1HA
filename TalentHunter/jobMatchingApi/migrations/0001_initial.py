# Generated by Django 2.0.2 on 2019-04-16 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_auto_20190416_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('publication_date', models.CharField(blank=True, max_length=50, null=True)),
                ('expiration_date', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('job_requirements', models.TextField(blank=True, null=True)),
                ('job_type', models.CharField(blank=True, max_length=100, null=True)),
                ('category_set', models.ManyToManyField(blank=True, null=True, to='jobMatchingApi.JobCategory')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offres', to='accounts.Recruiter')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]