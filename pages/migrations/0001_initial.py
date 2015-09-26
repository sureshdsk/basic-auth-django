# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_title', models.CharField(max_length=200)),
                ('page_slug', models.SlugField()),
                ('published_date', models.DateTimeField(verbose_name=b'date published')),
                ('page_content', models.TextField()),
            ],
        ),
    ]
