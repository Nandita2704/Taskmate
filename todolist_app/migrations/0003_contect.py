# Generated by Django 2.2.10 on 2021-06-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_tasklist_manage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=300)),
                ('name_last', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('enquiry', models.CharField(max_length=800)),
            ],
        ),
    ]