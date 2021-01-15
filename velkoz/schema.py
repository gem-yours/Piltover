from graphene_django import DjangoObjectType
import graphene

from .models import ChampionModel, SkillModel
from .championschema import CreateChampion, ChampionType
from .skillschema import CreateSkill, SkillType
from .fileschema import UploadMutation


class Query(graphene.ObjectType):
    champion = graphene.Field(ChampionType, champion_id=graphene.Int())
    all_champions = graphene.List(ChampionType)

    skill = graphene.Field(SkillType, skill_id=graphene.Int())
    all_skills = graphene.List(SkillType)

    @staticmethod
    def resolve_all_skills(self, info):
        return SkillModel.objects.all()

    @staticmethod
    def resolve_champion(self, info, **kwargs):
        champion_id = kwargs.get("champion_id")
        if champion_id is not None:
            return ChampionModel.objects.get(pk=champion_id)
        return None

    @staticmethod
    def resolve_skill(self, info, **kwargs):
        skill_id = kwargs.get("skill_id")
        if skill_id is not None:
            return SkillModel.objects.get(pk=skill_id)
        return None


class Mutations(graphene.ObjectType):
    create_skill = CreateSkill.Field()
    create_champion = CreateChampion.Field()
    upload_image = UploadMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
