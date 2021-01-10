from graphene_django import DjangoObjectType
import graphene
from .models import ChampionModel


class ChampionType(DjangoObjectType):
    class Meta:
        model = ChampionModel


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


def resolve_all_champions(info):
    return ChampionModel.objects.all()


class CreateChampion(graphene.Mutation):
    class Arguments:
        champion_data = ChampionInput(required=True)

    champion = graphene.Field(ChampionType)

    def mutate(self, info, champion_data):
        champion = ChampionModel.objects.create(**champion_data)
        return CreateChampion(champion=champion)