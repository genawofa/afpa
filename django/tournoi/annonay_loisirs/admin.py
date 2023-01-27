from django.contrib import admin
from .models import Participant
from .models import Equipe
from .models import Match


# Register your models here.
admin.site.register(Participant)
admin.site.register(Equipe)
admin.site.register(Match)

