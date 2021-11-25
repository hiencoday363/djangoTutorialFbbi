from django.db import models

# Create your models here.

class Live_stream(models.Model):
    choice_status = (
        (0, "Live streaming hasn't started yet"),
        (1, 'Live streaming started'),
        (2, 'Live '))
    choice_available = (
        (0, "Not available"),
        (1, 'Available'))
    id = models.AutoField(primary_key=True)
    ivs_arn = models.CharField(null=True, max_length=255)
    status = models.SmallIntegerField(choices=choice_status)
    host_user_id = models.IntegerField()
    performance_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255, null=True)
    ingest_endpoints = models.CharField(max_length=255)
    stream_key = models.CharField(max_length=255)
    playback_url = models.CharField(max_length=255)
    comment_available_flag = models.SmallIntegerField(choices=choice_available)
    tipping_available_flag = models.SmallIntegerField(choices=choice_available)
    stamps_granted = models.DecimalField(max_digits=15, decimal_places=0)
    release_datetime = models.DateTimeField(auto_now_add=True)
    start_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField(auto_now_add=True)
    total_number_of_viewers = models.IntegerField(null=True)
    seconds_delivered = models.DecimalField(max_digits=15, decimal_places=0)
    chanel_id_sd = models.CharField(max_length=255, null=True)
    chanel_id_fhd = models.CharField(max_length=255, null=True)
    input_id_sd = models.CharField(max_length=255, null=True)
    input_id_fhd = models.CharField(max_length=255, null=True)
    video_url_sd = models.CharField(max_length=255, null=True)
    video_url_fhd = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.live_stream


class Live_stream_viewer(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User.User", on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
