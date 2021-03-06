# Generated by Django 3.0.3 on 2021-01-25 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_emailevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default=None, max_length=64)),
                ('phoneNumber', models.CharField(default=None, max_length=64)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='EmailEvents',
        ),
        migrations.RenameField(
            model_name='fixedexpense',
            old_name='ownear',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='variableexpense',
            old_name='ownear',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='notificationevents',
            name='expense',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.FixedExpense'),
        ),
    ]
