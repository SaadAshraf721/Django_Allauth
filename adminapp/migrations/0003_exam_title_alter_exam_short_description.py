# Generated by Django 4.0 on 2021-12-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_exam_sts'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='title',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exam',
            name='short_description',
            field=models.CharField(max_length=2400),
        ),
    ]
