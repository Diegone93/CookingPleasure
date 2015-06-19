from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100, primary_key=True)
    mail = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.nickname)


class Recipe(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    user = models.ForeignKey(User.nickname)

    def __unicode__(self):
        return u'%s' % (self.name)

# Switch tables BEGIN
class RecipeMenuContains(models.Model):
    menu_id = models.ForeignKey(Menu.auto_increment_id)
    recipe_id = models.ForeignKey(Recipe.auto_increment_id)


class RecipeIngredientContains(models.Model):
    recipe_id = models.ForeignKey(Recipe.auto_increment_id)
    ingredient_name = models.ForeignKey(Ingredient.name)

class ListIngredientContains(models.Model):
    ingredient_name = models.ForeignKey(Ingredient.name)
    list_id = models.ForeignKey(List.auto_increment_id)
# Switch tables END

class Ingredient(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Menu(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User.nickname)

    def __unicode__(self):
        return u'%s' % (self.name)

class List(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User.nickname)

    def __unicode__(self):
        return u'%s' % (self.name)
