
from django.contrib import admin
from .models import Bb
from .models import Rubric
...
admin.site.register(Rubric)



# Register your models here.
class BbAdmin(admin.ModelAdmin):
  list_display = ('title', 'content', 'price', 'published', 'rubric')
  list_display_links = ('title', 'content')
  search_fields = ('title', 'content', 'price', 'published')

admin.site.register(Bb, BbAdmin)
