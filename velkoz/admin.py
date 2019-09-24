from django.contrib import admin

from .models import ChampionModel, SkillModel

admin.site.register(ChampionModel)
admin.site.register(SkillModel)
