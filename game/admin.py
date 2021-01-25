from django.contrib import admin
from .models import MobileSuit, Helm, Chest, LeftArm, RightArm, Legs, Modifier, Enemy

# Register your models here.

admin.site.register(MobileSuit)
admin.site.register(Helm)
admin.site.register(Chest)
admin.site.register(LeftArm)
admin.site.register(RightArm)
admin.site.register(Legs)
admin.site.register(Modifier)
admin.site.register(Enemy)