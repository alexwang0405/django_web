from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Clock(models.Model):

    CLOCK_TYPE = (
        ('0', '上班'),
        ('1', '下班')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clock_type = models.CharField(choices=CLOCK_TYPE, max_length=2)  # 上班or下班
    clock_time = models.DateTimeField(default=timezone.now)
