# from django.contrib.auth import authenticate
# from apps.User.models import User
# import os
# from rest_framework.exceptions import AuthenticationFailed
# from datetime import datetime
#
#
# def generate_nickname(name):
#     nickname = "".join(name.split(' ')).lower()
#     if not User.objects.filter(nickname=nickname).exists():
#         return nickname
#     else:
#         timestamp = str(datetime.now().timestamp())
#         str_time = "".join(timestamp.split('.'))
#         return nickname + str_time
#
#
# def register_social_user(provider, user_id, email, name):
#     user_by_email = User.objects.filter(email=email).first()
#
#     if user_by_email.exists():
#
#         if provider == user_by_email.auth_provider:
#
#             registered_user = authenticate(email=email, password=os.environ.get('PASSWORD_DEFAULT'))
#
#             return {
#                 'nickname': registered_user.nickname,
#                 'email': registered_user.email,
#                 'tokens': registered_user.tokens()}
#
#         else:
#             raise AuthenticationFailed(
#                 detail='Please continue your login using ' + user_by_email.auth_provider)
#
#     else:
#         user = {
#             'nickname': generate_nickname(name),
#             'email': email,
#             'password': os.environ.get('PASSWORD_DEFAULT')
#         }
#         # 'password': os.environ.get('SOCIAL_SECRET')
#
#         user = User.objects.create_user(**user)
#         user.is_active = True
#         user.auth_provider = provider
#         user.save()
#
#         new_user = authenticate(
#             email=email, password=os.environ.get('PASSWORD_DEFAULT'))
#         return {
#             'email': new_user.email,
#             'username': new_user.username,
#             'tokens': new_user.tokens()
#         }
