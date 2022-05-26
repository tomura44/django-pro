# Generated by Django 3.1.7 on 2022-04-21 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certifications', '0004_experiences_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiences',
            name='advices',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='experiences',
            name='common_test_score',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='experiences',
            name='cram',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='experiences',
            name='study_method',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='experiences',
            name='description',
            field=models.TextField(blank=True, default='', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='experiences',
            name='how_to_study',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='experiences',
            name='how_to_study_site',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='experiences',
            name='score',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='experiences',
            name='study_time',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
