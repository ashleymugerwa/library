from django.contrib import admin
from . import models


class StudentAdmin(admin.ModelAdmin):
    model = models.Student
    list_display = ('excerpt', )

    @staticmethod
    def excerpt(obj):
        return obj.get_excerpt(5)


admin.site.register(models.Student, StudentAdmin)
