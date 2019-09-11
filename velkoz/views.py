from rest_framework import viewsets, filters

from .models import Champion, Skill
from .serializer import ChampionSerializer, SkillSerializer


class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

