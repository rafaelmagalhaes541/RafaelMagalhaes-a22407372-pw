from django.contrib.auth.models import User
from django.db import models

# Create your models here.
User.add_to_class('token', models.CharField(max_length=100, null=True, blank=True))