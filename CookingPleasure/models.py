from django.db import models
from django import forms

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100, primary_key=True)
    mail = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.nickname)


class Recipe(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % (self.name)

class Ingredient(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    recipe = models.ForeignKey(Recipe)
    list = models.ForeignKey(List)

    def __unicode__(self):
        return u'%s' % (self.name)

class Menu(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % (self.name)

class List(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % (self.name)
