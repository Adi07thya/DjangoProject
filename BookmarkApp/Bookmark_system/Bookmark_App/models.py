from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """ Customers table containing their geolocation."""

    latitude    = models.DecimalField(max_digits=19, decimal_places=16)
    longitude   = models.DecimalField(max_digits=19, decimal_places=16)


class Bookmark(models.Model):
    """ Bookmark table conatining title ,url ,source_name """

    customer    = models.ForeignKey(Customer,on_delete=models.CASCADE)
    title       = models.CharField(max_length=200)
    urls        = models.URLField(max_length = 200)
    source_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title



class CustomerBookmark(models.Model):
    """  Customer Bookmark table which has relationship between Customer and Bookmark """
    customer    = models.ForeignKey(Customer,on_delete=models.CASCADE,)
    bookmark    = models.ForeignKey(Bookmark,on_delete=models.CASCADE)
