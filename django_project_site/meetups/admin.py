from django.contrib import admin
from .models import Location, Meetup, Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location') # columns displaying on django admin
    list_filter = ('location', 'date') # filter by
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)