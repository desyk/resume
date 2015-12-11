from django.db import models
from django.contrib.auth.models import AbstractUser
# from datetime import datetime

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, default='')
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'auth_user'
