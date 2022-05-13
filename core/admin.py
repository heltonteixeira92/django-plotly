from django.contrib import admin
from core.models import Repository, Commit

# Register your models here.
admin.site.register(Repository)
admin.site.register(Commit)
