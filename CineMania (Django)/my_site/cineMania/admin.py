from django.contrib import admin
from .models import Film, Actors, Contacts, Workers, \
    CinemaStudio, Feedback, CastingParticipants, Questionnaire

admin.site.register(Film)
admin.site.register(Contacts)
admin.site.register(Actors)
admin.site.register(Workers)
admin.site.register(CinemaStudio)
admin.site.register(Questionnaire)
admin.site.register(CastingParticipants)
admin.site.register(Feedback)
