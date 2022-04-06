from django.contrib import admin
# from taggit.models import Tag
from .models import Block, Material, Category, Condition, Geometry, Symbol, Photo, Color, Unit




class PhotoTabularInline(admin.TabularInline):
	model = Photo

class BlockAdmin(admin.ModelAdmin):
	inlines = [PhotoTabularInline]
	model = Block
	list_display = ['name']


# Register your models here.



admin.site.register(Block, BlockAdmin)
admin.site.register(Material)
admin.site.register(Category)
admin.site.register(Condition)
admin.site.register( Geometry )
admin.site.register(Symbol)
admin.site.register(Photo)
# admin.site.register(Tag)
admin.site.register(Color)
admin.site.register(Unit)
