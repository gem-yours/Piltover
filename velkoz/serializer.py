from rest_framework import serializers

from .models import Champion, Skill


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = ['name',
                  'japanese_name',
                  'health',
                  'health_growth',
                  'health_regen',
                  'health_regen_growth'
                  ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'description']
