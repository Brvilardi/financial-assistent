# Generated by Django 3.1.5 on 2021-01-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20210125_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixedexpense',
            name='begining',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]