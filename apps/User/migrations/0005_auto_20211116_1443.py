# Generated by Django 3.2.9 on 2021-11-16 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MasterData', '0001_initial'),
        ('Event', '0001_initial'),
        ('User', '0004_user_prefecture_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_path',
            name='box_notification_trans_content_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MasterData.box_notification_trans_content'),
        ),
        migrations.AlterField(
            model_name='image_path',
            name='event_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='img_path', to='Event.events'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]