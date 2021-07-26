from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Model, OneToOneField, CharField, CASCADE
from django.db import models
# from orders.models import Order

# Create your models here.
class Clients(Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = CharField(max_length=30,  help_text='Optional.')
    last_name = CharField(max_length=30,  help_text='Optional.')
    address = CharField(max_length=400)
    phoneNumber = CharField(max_length=11)
    phone = CharField(max_length=12)
    def __str__(self):
        return str(self.user)



class Titelrules(Model):
    titel = models.CharField(max_length=400)

    def __str__(self):
        return self.titel
class Rules(Model):
    statement = models.CharField(max_length=800)

    def __str__(self):
        return self.statement