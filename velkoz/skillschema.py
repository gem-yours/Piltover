from graphene_django import DjangoObjectType
import graphene
from .models import SkillModel


class SkillType(DjangoObjectType):
    class Meta:
        model = SkillModel


class SkillInput(graphene.InputObjectType):
    name = graphene.String()
    patch = graphene.String()
    base_damage = graphene.Int()
    ap_ratio = graphene.Float()
    ad_ratio = graphene.Float()
    base_damage_growth = graphene.Int()
    ap_ratio_growth = graphene.Float()
    ad_ratio_growth = graphene.Float()
    description = graphene.String()


class CreateSkill(graphene.Mutation):
    class Arguments:
        skill_data = SkillInput(required=True)

    skill = graphene.Field(SkillType)

    def mutate(self, info, skill_data):
        skill = SkillModel.objects.create(**skill_data)
        return CreateSkill(skill=skill)
