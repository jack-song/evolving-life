# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geography',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.TextField(unique=True)),
                ('colour', models.IntegerField(unique=True)),
                ('symbol', models.CharField(unique=True, max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeographyPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('geography', models.ForeignKey(to='evolvinglife.Geography')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('colour', models.IntegerField(unique=True)),
                ('symbol', models.CharField(unique=True, max_length=1)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('user', models.ForeignKey(to='evolvinglife.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
