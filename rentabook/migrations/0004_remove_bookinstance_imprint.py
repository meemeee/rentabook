# Generated by Django 2.1.5 on 2019-12-09 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentabook', '0003_auto_20191209_0357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='imprint',
        ),
    ]
