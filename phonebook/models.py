from django.urls import reverse
from django.db import models
from login.models import User

class Contact(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    contactname = models.CharField(max_length=100,null=False,blank=False)
    number = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self. contactname

    def get_abs_update_path(self):
        return reverse("phonebook:update-contact-view", kwargs={'name': self.contactname})
        
    def get_abs_delete_path(self):
        return reverse("phonebook:delete-contact", kwargs={'name': self.contactname})
    
    def get_abs_upt_path(self):
        return reverse("phonebook:update-contact", kwargs={'id': self.id})

