from polls.models import Poll, Choice
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)