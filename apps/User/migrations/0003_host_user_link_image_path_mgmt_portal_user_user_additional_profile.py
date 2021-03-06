# Generated by Django 3.2.9 on 2021-11-15 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Livestream', '0001_initial'),
        ('Event', '0001_initial'),
        ('MasterData', '0001_initial'),
        ('User', '0002_auto_20211115_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_additional_profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('additional_profile_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterData.additional_profile_item')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mgmt_portal_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type', models.IntegerField(choices=[(1, 'System admin user'), (2, 'Client user'), (3, 'Host user')], default=1)),
                ('email', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('remember_token', models.CharField(max_length=255, null=True)),
                ('is_archived', models.IntegerField(choices=[(0, 'Not archived'), (1, 'Archived')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='User.client')),
            ],
        ),
        migrations.CreateModel(
            name='Image_path',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('dir_path', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('display_order', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('box_notification_trans_content_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MasterData.box_notification_trans_content')),
                ('event_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Event.events')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Host_user_link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('host_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Livestream.live_stream')),
            ],
        ),
    ]
