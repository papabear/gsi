from gsi.projects.models import Project, Pushlist, Status
from django.contrib import admin

class PushlistInline(admin.StackedInline):
    model = Pushlist
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PushlistInline,
    ]
    list_filter = ['status']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Status)
admin.site.register(Pushlist)