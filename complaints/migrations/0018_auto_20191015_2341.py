# Generated by Django 2.2.4 on 2019-10-15 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0017_auto_20190919_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
