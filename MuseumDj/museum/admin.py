from django.contrib import admin
from .models import Hall, Exhibit
from .models import Collection
# Register your models here.
admin.site.register([Hall, Collection, Exhibit])
