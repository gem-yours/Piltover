from graphene_django import DjangoObjectType
import graphene
from .models import ChampionModel, SkillModel


class ChampionType(DjangoObjectType):
    class Meta:
        model = ChampionModel


class SKillType(DjangoObjectType):
    class Meta:
        model = SkillModel


class Query(graphene.ObjectType):
    champion = graphene.Field(ChampionType, champion_id=graphene.Int())
    all_champions = graphene.List(ChampionType)

    skill = graphene.Field(SKillType, skill_id=graphene.Int())
    all_skills = graphene.List(SKillType)

    def resolve_all_champions(self, info):
        return ChampionModel.objects.all()

    def resolve_all_skills(self, info):
        return SkillModel.objects.all()

    def resolve_champion(self, info, **kwargs):
        id = kwargs.get("champion_id")
        if id is not None:
            return ChampionModel.objects.get(pk=id)
        return None

    def resolve_skill(self, info, **kwargs):
        id = kwargs.get("skill_id")
        if id is not None:
            return SkillModel.objects.get(pk=id)
        return None


schema = graphene.Schema(query=Query)
