from django.db import models
import uuid
from taggit.managers import TaggableManager

# Create your models here.


class Common(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Material(Common):
    pass


class Geometry(Common):
    pass

class Unit(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Symbol(Common):
    pass


class Condition(Common):
    code = models.CharField(max_length=50)


class Color(models.Model):
    name = models.CharField(max_length=50)
    R = models.IntegerField()
    G = models.IntegerField()
    B = models.IntegerField()

    def __str__(self):
        return self.name


class Category(Common):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)


#class Tag(models.Model):
#    title = models.CharField(max_length=30)
#    #blocks = models.ManyToManyField(Block)

#    class Meta:
#        ordering = ['title']

#    def __str__(self):
#        return self.title




class Block(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag, blank=True)
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    #photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    #photo = models.ManyToManyField(Photo, unique=True)
    # amount_units = models.CharField(max_length=30, blank=True, null=True)
    # severity_units = models.CharField(max_length=30, blank=True, null=True)
    amount_units = models.ForeignKey(Unit, blank=True, null=True, on_delete=models.CASCADE, related_name="b")
    severity_units = models.ForeignKey(Unit, blank=True, null=True, on_delete=models.CASCADE, related_name="a")
    slug = models.SlugField(unique=True, max_length=100, default=uuid.uuid1)
    tags = TaggableManager()
    guid = models.UUIDField(
        primary_key=False,
        default=uuid.uuid4,
        editable=True,
        null=True,
        unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=500)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title
