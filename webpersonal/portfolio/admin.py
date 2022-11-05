from django.contrib import admin
from .models import Project


# Register your models here.
# Para permitir ver los campos de Fecha de creación y de modificacion
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
