# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Roomtype(models.Model):

    #__Roomtype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    base_price = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    #__Roomtype_FIELDS__END

    class Meta:
        verbose_name        = _("Roomtype")
        verbose_name_plural = _("Roomtype")


class Hotel(models.Model):

    #__Hotel_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)

    #__Hotel_FIELDS__END

    class Meta:
        verbose_name        = _("Hotel")
        verbose_name_plural = _("Hotel")


class Room(models.Model):

    #__Room_FIELDS__
    room_number = models.IntegerField(null=True, blank=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    features = models.TextField(max_length=255, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    #__Room_FIELDS__END

    class Meta:
        verbose_name        = _("Room")
        verbose_name_plural = _("Room")



#__MODELS__END
