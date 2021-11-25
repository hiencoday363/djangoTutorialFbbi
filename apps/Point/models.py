from django.db import models


# Create your models here.

class User_point(models.Model):
    choice_type = (
        (1, 'Deposit'),
        (2, 'Withdrawal'))
    choice_withdrawal = (
        (1, 'Exchange for a gift'),
        (2, 'Exchange for a ticket'))
    choice_deposit = (
        (1, 'Purchase'),)
    user_id = models.ForeignKey("User.User", on_delete=models.CASCADE)
    type = models.IntegerField(choices=choice_type, default=1)
    deposit_reason = models.IntegerField(null=True, choices=choice_deposit)
    withdrawal_reason = models.IntegerField(null=True, choices=choice_withdrawal)
    points = models.DecimalField(max_digits=15, decimal_places=0)
    transacted_at = models.DateTimeField(auto_now_add=True)
    points_balance = models.DecimalField(max_digits=15, decimal_places=0)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)


class Points_package(models.Model):
    client = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    apple_product_id = models.CharField(max_length=255, null=True)
    google_product_id = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=0)
    points = models.DecimalField(max_digits=15, decimal_places=0)
    display_order = models.SmallIntegerField()
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.name


class Points_package_history(models.Model):
    user_point = models.ForeignKey(User_point, on_delete=models.CASCADE)
    points_package_id = models.ForeignKey(Points_package, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=15, decimal_places=0)
    purchased_at = models.DateField(auto_now_add=True)
    apple_trans_id = models.CharField(max_length=255, null=True)
    google_trans_id = models.CharField(max_length=255, null=True)
    apple_receipt = models.TextField(null=True)
    google_receipt = models.TextField(null=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)


class Gift(models.Model):
    client_id = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    points_spent = models.DecimalField(max_digits=15, decimal_places=0)
    image_url = models.CharField(max_length=255)
    display_order = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class User_gift(models.Model):
    choice_status = (
        (0, 'Unused'),
        (1, 'Used'))
    user_id = models.ForeignKey("User.User", on_delete=models.CASCADE)
    gift_id = models.ForeignKey(Gift, on_delete=models.CASCADE)
    status = models.IntegerField(choices=choice_status, default=1)
    used_at = models.DateTimeField(null=True, auto_now_add=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)


class Point_spending_history(models.Model):
    user_point_id = models.ForeignKey(User_point, on_delete=models.CASCADE)
    user_gift_id = models.ForeignKey(User_gift, on_delete=models.CASCADE)
    spent_at = models.DateTimeField(null=False, auto_now_add=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)


class User_stamp(models.Model):
    choice_type = (
        (1, 'Deposit'),
        (2, 'Withdrawal'))
    choice_deposit = (
        (1, 'Participation in a performance'),
        (2, 'Application of a stamp code'))
    choice_withdrawal = (
        (1, 'Exchange for a ticket'),)
    user_id = models.ForeignKey("User.User", on_delete=models.CASCADE)
    type = models.IntegerField(default=1, choices=choice_type)
    deposit_reason = models.IntegerField(null=True, choices=choice_deposit)
    withdrawal_reason = models.IntegerField(null=True, choices=choice_withdrawal)
    stamps = models.DecimalField(max_digits=15, decimal_places=0)
    transacted_at = models.DateTimeField(auto_now_add=True)
    stamps_balance = models.DecimalField(max_digits=15, decimal_places=0)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)




class Gift_purchase_history(models.Model):
    user_gift_id = models.ForeignKey(User_gift, on_delete=models.CASCADE)
    user_point_id = models.ForeignKey(User_point, on_delete=models.CASCADE)
    points_spent = models.DecimalField(max_digits=15, decimal_places=0)
    purchased_at = models.DateTimeField(null=False, auto_now_add=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)


class Gift_tipping_history(models.Model):
    user_gift_id = models.ForeignKey(User_gift, on_delete=models.CASCADE)
    to_user_id = models.ForeignKey("MasterData.Box_notification_trans_content", on_delete=models.CASCADE)
    points_equivalent = models.DecimalField(max_digits=15, decimal_places=0)
    tipped_at = models.DateTimeField(null=False, auto_now_add=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)


class Stamps_code(models.Model):
    client_id = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    stamps_granted = models.DecimalField(max_digits=15, decimal_places=0)
    number_of_applicable_user = models.IntegerField(null=True)
    number_of_applied_user = models.IntegerField()
    expires_in = models.DateTimeField(null=False, auto_now_add=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.name


class Follow(models.Model):
    from_user_id = models.IntegerField()
    to_user_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ranking(models.Model):
    choice_type = (
        (1, 'Tipping'),
        (2, 'Tipped')
    )
    client_id = models.ForeignKey("User.Client", on_delete=models.CASCADE)
    type = models.SmallIntegerField(choices=choice_type, default=1)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)


class Ranking_summary(models.Model):
    ranking_id = models.ForeignKey(Ranking, on_delete=models.CASCADE)
    user_id = models.ForeignKey("User.User", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=0)
    target_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
