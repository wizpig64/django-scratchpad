from django.contrib import admin
from scratchpad.models import Note

class NoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Note, NoteAdmin)
