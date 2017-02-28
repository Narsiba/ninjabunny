# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 04:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('galleries', '0002_auto_20141227_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('topheading', models.CharField(blank=True, help_text=b'The top heading of the carousel caption', max_length=200)),
                ('headline', models.CharField(blank=True, help_text=b'The Headline in the middle of the carousel caption', max_length=200)),
                ('subheading', models.CharField(blank=True, help_text=b'The subheading of the carousel caption', max_length=200)),
                ('buttontext', models.CharField(blank=True, help_text=b'The text on the button to enter the page', max_length=200)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Home page',
                'verbose_name_plural': 'Home pages',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image')),
                ('title', models.CharField(default=b'Slide', max_length=50)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='rtwtheme.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
        migrations.CreateModel(
            name='VideoURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('video_url', models.URLField(blank=True, verbose_name='Video')),
                ('title', models.CharField(default=b'Video', max_length=50)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='galleries.Gallery')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
