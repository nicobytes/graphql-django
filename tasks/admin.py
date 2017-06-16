from django.contrib import admin

from tasks.models import Task, Category, Food

# Register your models here.
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Food)