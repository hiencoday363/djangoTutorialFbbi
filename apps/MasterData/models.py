from django.db import models

from apps.Point.models import User_stamp


class Prefectures(models.Model):
    choice_default = (
        (0, 'Not default'),
        (1, 'Default'))
    name = models.CharField(max_length=45, null=False)
    display_order = models.SmallIntegerField(null=False)
    is_default = models.SmallIntegerField(null=False, choices=choice_default)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.name


class Stamp_receipt_history(models.Model):
    user_stamp_id = models.ForeignKey(User_stamp, on_delete=models.CASCADE)
    live_stream_id = models.IntegerField(null=True)
    stamp_code_id = models.IntegerField(null=True)
    received_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Stamp_spending_history(models.Model):
    choice_spend = (
        (1, 'Ticket'),
    )
    user_stamp_id = models.ForeignKey("Point.User_stamp", on_delete=models.CASCADE)
    spent_for = models.SmallIntegerField(choices=choice_spend, default=1)
    stamp_code_id = models.IntegerField(null=True)
    spent_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Additional_profile_item(models.Model):
    name = models.CharField(max_length=255)
    display_order = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Push_notification_master_content(models.Model):
    choice_timing = (
        (1, 'When a livestream event is created'),
        (2, 'When an office event is created'),
        (3, 'When a drawing winner determined'),
        (4, 'When a livestream starts in 10 minutes'),
        (5, 'When tickets purchase is complete'),
        (99, 'Any timing')
    )
    client_id = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    timing_type = models.SmallIntegerField(choices=choice_timing, default=1)
    title = models.CharField(max_length=255, null=True)
    body = models.TextField()
    internal_url = models.CharField(max_length=255, null=True)
    memo = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body


class Push_notification_trans_content(models.Model):
    choice_deliver = (
        (0, 'Not delivered'),
        (1, 'Delivered'))
    client_id = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    body = models.TextField()
    internal_url = models.CharField(max_length=255, null=True)
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField(auto_now_add=True)
    is_delivered = models.IntegerField(choices=choice_deliver)
    delivered_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body


class Push_notification(models.Model):
    choice_platform = (
        (1, 'IOS'),
        (2, 'Android')
    )
    choice_status = (
        (0, 'Not sent'),
        (1, 'Sent')
    )
    user_id = models.ForeignKey("User.User", on_delete=models.CASCADE)
    to_platform = models.SmallIntegerField(choices=choice_platform, default=1)
    title = models.CharField(max_length=255, null=True)
    body = models.TextField()
    internal_url = models.CharField(max_length=255, null=True)
    scheduled_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(choices=choice_status, default=1)
    sent_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sent_relation(models.Model):
    event_id = models.IntegerField(null=True)
    live_stream_id = models.IntegerField(null=True)
    email_notification_trans_content_id = models.IntegerField(null=True)
    push_notification_trans_content_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Email_auth(models.Model):
    choice_type = (
        (1, 'General user'),
        (2, 'Host user'),
        (3, 'Mgmt portal user')
    )
    user_type = models.SmallIntegerField(choices=choice_type, default=1)
    email = models.CharField(max_length=254)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Password_reset(models.Model):
    choice_type = (
        (1, 'General user'),
        (2, 'Host user'),
        (3, 'Mgmt portal user')
    )
    id = models.AutoField(primary_key=True)
    user_type = models.SmallIntegerField(choices=choice_type, default=1)
    email = models.CharField(max_length=254)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Refresh_token(models.Model):
    choice = (
        (0, 'Not blacklisted'),
        (2, 'Blacklisted')
    )
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField(null=True)
    mgmt_portal_user_id = models.IntegerField(null=True)
    encrypted_refresh_token = models.CharField(max_length=255)
    expires_in = models.DateTimeField(auto_now_add=True)
    is_blacklisted = models.SmallIntegerField(choices=choice, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Device_token(models.Model):
    choice_platform = (
        (1, 'IOS'),
        (2, 'Android')
    )
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    platform = models.SmallIntegerField(choices=choice_platform, default=1)
    title = models.CharField(max_length=255, null=True)
    token = models.CharField(max_length=255)
    invalidated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Related_link(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    dir_path = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    display_order = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Email_notification_master_content(models.Model):
    choice_timing = (
        (1, 'When a drawing winner determined'),
        (2, 'When tickets purchase is complete'),
        (99, 'Any timing')
    )
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    timing_type = models.SmallIntegerField(choices=choice_timing, default=1)
    title = models.CharField(max_length=255, null=True)
    body = models.TextField()
    memo = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Email_notification_trans_content(models.Model):
    choice_deliver = (
        (0, 'Not delivered'),
        (1, 'Delivered')
    )
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField(auto_now_add=True)
    is_delivered = models.SmallIntegerField(choices=choice_deliver, default=1)
    delivered_at = models.DateTimeField(null=True, auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Email_notification(models.Model):
    choice_status = (
        (0, 'Not sent'),
        (1, 'Sent'),
        (2, 'Error')
    )
    id = models.AutoField(primary_key=True)
    to_email = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    body = models.TextField()
    scheduled_at = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=choice_status, default=1)
    sent_at = models.DateTimeField(null=True, auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Box_notification_trans_content(models.Model):
    choice_type = (
        (1, 'Host user'),
        (2, 'Client user (Mgmt portal user)'),
        (3, 'System admin user( Mgmt portal user)'))
    choice_deliver = (
        (0, 'Not delivered'),
        (1, 'Delivered'))
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    from_type = models.IntegerField(choices=choice_type, default=1)
    from_user_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField(auto_now_add=True)
    is_delivered = models.IntegerField(choices=choice_deliver)
    delivered_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Box_notification_master_content(models.Model):
    choice_timing = (
        (99, 'Any timing'),
    )
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    timing_type = models.SmallIntegerField(choices=choice_timing, default=99)
    title = models.CharField(max_length=255)
    body = models.TextField()
    memo = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Box_notification(models.Model):
    choice_read = (
        (0, 'Not read'),
        (1, 'Read')
    )
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("User.User", on_delete=models.CASCADE)
    box_notification_master_content_id = models.ForeignKey(Box_notification_master_content, on_delete=models.SET_NULL,
                                                           null=True)
    box_notification_trans_content_id = models.ForeignKey(Box_notification_trans_content, on_delete=models.SET_NULL,
                                                          null=True)
    is_read = models.SmallIntegerField(choices=choice_read, default=1)
    read_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
