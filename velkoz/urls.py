from rest_framework import routers

# from .views import ChampionViewSet, SkillViewSet
from .views import  SkillViewSet

router = routers.SimpleRouter()
# router.register('champion', ChampionViewSet, basename='champion')
router.register('skill', SkillViewSet, basename='skill')

