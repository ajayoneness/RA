from django.contrib import admin
from . import models


admin.site.register(models.category)
admin.site.register(models.quotes)
admin.site.register(models.contactform)
