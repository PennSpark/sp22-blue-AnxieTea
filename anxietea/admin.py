from django.contrib import admin

# Register your models here.
from .models import User
admin.site.register(User)

from .models import Analysis
admin.site.register(Analysis)

