# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

