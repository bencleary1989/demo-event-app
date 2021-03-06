# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendeeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee_uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('attendee_name', models.CharField(max_length=255, verbose_name='Name')),
                ('attendee_email', models.CharField(max_length=255, verbose_name='Email')),
                ('attendee_job_title', models.CharField(max_length=150, verbose_name='Job Title')),
                ('attendee_company', models.CharField(max_length=255, verbose_name='Company')),
                ('attendee_profile', models.TextField(verbose_name='Your Profile')),
                ('attendee_image', models.ImageField(upload_to=b'', verbose_name='Profile Picture')),
                ('attendee_phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone Number')),
                ('attendee_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Website URL')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Attendee',
                'db_table': 'demo_attendee_details',
                'managed': True,
                'verbose_name_plural': 'Attendees',
            },
        ),
        migrations.CreateModel(
            name='AttendeeNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendee_notes', to='event_attendees.AttendeeDetails', to_field='attendee_uid')),
            ],
            options={
                'verbose_name': 'Attendee Note',
                'db_table': 'demo_attendee_notes',
                'managed': True,
                'verbose_name_plural': 'Attendee Notes',
            },
        ),
    ]
