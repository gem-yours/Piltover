from graphene_django import DjangoObjectType
import graphene
from .models import ChampionModel, SkillModel


class ChampionType(DjangoObjectType):
    class Meta:
        model = ChampionModel


class SkillType(DjangoObjectType):
    class Meta:
        model = SkillModel


def resolve_all_champions(info):
    return ChampionModel.objects.all()


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


class ChampionInput(graphene.InputObjectType):
    name = graphene.String()
    japanese_name = graphene.String()
    patch = graphene.String()
    health = graphene.Float()
    health_growth = graphene.Float()
    health_regen = graphene.Float()
    health_regen_growth = graphene.Float()
    resource_name = graphene.String()
    resource = graphene.Float()
    resource_growth = graphene.Float()
    resource_regen = graphene.Float()
    resource_regen_growth = graphene.Float()
    attack_range = graphene.Float()
    attack_damage = graphene.Float()
    attack_damage_growth = graphene.Float()
    attack_speed = graphene.Float()
    attack_speed_growth = graphene.Float()
    armor = graphene.Float()
    armor_growth = graphene.Float()
    magic_resist = graphene.Float()
    magic_resist_growth = graphene.Float()
    move_speed = graphene.Int()

    # TODO: disable SkillInputs because ddragon static data is broken
    # pls Riot...
    # passive = graphene.Field(SkillInput)
    # q = graphene.Field(SkillInput)
    # w = graphene.Field(SkillInput)
    # e = graphene.Field(SkillInput)
    # r = graphene.Field(SkillInput)


class CreateChampion(graphene.Mutation):
    class Arguments:
        champion_data = ChampionInput(required=True)

    champion = graphene.Field(ChampionType)

    def mutate(self, info, champion_data):
        champion = ChampionModel.objects.create(**champion_data)
        return CreateChampion(champion=champion)


class Mutations(graphene.ObjectType):
    create_skill = CreateSkill.Field()
    create_champion = CreateChampion.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
