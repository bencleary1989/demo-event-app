# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import event_speakers.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventSpeakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('speaker_name', models.CharField(max_length=255, verbose_name='Speaker Name')),
                ('speaker_topic', models.CharField(blank=True, max_length=255, verbose_name='Speaker Topic')),
                ('speaker_image', models.ImageField(blank=True, upload_to=event_speakers.models.imageuploadeto)),
                ('talk_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Event Speaker',
                'db_table': 'demo_event_speakers',
                'managed': True,
                'verbose_name_plural': 'Event Speakers',
            },
        ),
        migrations.CreateModel(
            name='SpeakerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('speaker_email', models.CharField(blank=True, max_length=255)),
                ('speaker_location', models.CharField(blank=True, max_length=255)),
                ('speaker_url', models.CharField(blank=True, max_length=255)),
                ('speaker_profile', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Speaker Profile',
                'db_table': 'demo_speaker_profiles',
                'managed': True,
                'verbose_name_plural': 'Speaker Profiles',
            },
        ),
        migrations.AddField(
            model_name='eventspeakers',
            name='speaker_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_speakers.SpeakerProfile', to_field='profile_uid'),
        ),
    ]