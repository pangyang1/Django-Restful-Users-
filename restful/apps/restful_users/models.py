from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def adduser(self, postData):
        adduser = User.objects.create(name=postData['name'], email=postData['email'])
        return adduser
    def delete(self, id):
        delete =self.get(id=id)
        delete.delete()
        return delete
    def update(self, id, postData):
        update =self.get(id=id)
        update.name=postData['name']
        update.email=postData['email']
        update.save()
        return update

class User(models.Model):
    name = models.CharField(max_length =255)
    email = models.CharField(max_length =255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


# Create your models here.
