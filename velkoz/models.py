from django.db import models


class SkillModel(models.Model):
    @staticmethod
    def get_queryset():
        skills = SkillModel.objects_all()

    skill_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=32)

    base_damage = models.IntegerField(default=0)
    ad_ratio = models.FloatField(default=0)
    ap_ratio = models.FloatField(default=0)
    base_damage_growth = models.IntegerField(default=0)
    ad_ratio_growth = models.FloatField(default=0)
    ap_ratio_growth = models.FloatField(default=0)

    description = models.TextField()

    def __str__(self):
        return self.name


class ChampionModel(models.Model):
    @staticmethod
    def get_queryset():
        champions = ChampionModel.objects_all()

    champion_id = models.AutoField(primary_key=True, editable=False)

    name = models.CharField(max_length=16, null=False)
    japanese_name = models.CharField(max_length=16, null=False)
    image = models.ImageField(default=None, upload_to='champion_icon')

    health = models.FloatField(default=0)
    health_growth = models.FloatField(default=0)
    health_regen = models.FloatField(default=0)
    health_regen_growth = models.FloatField(default=0)

    resource_name = models.CharField(max_length=16, null=False, default="undefined")
    resource = models.FloatField(default=0)
    resource_growth = models.FloatField(default=0)
    resource_regen = models.FloatField(default=0)
    resource_regen_growth = models.FloatField(default=0)

    attack_range = models.FloatField(default=0)
    attack_damage = models.FloatField(default=0)
    attack_damage_growth = models.FloatField(default=0)
    attack_speed = models.FloatField(default=0)
    attack_speed_growth = models.FloatField(default=0)

    armor = models.IntegerField(default=0)
    armor_growth = models.FloatField(default=0)
    magic_resist = models.FloatField(default=0)
    magic_resist_growth = models.FloatField(default=0)
    move_speed = models.IntegerField(default=0)

    # TODO: disable SkillInputs because ddragon static data is broken
    # passive = models.ForeignKey(SkillModel, related_name='passive', on_delete=models.SET_NULL, null=True)
    # q = models.ForeignKey(SkillModel, related_name='q', on_delete=models.SET_NULL, null=True)
    # w = models.ForeignKey(SkillModel, related_name='w', on_delete=models.SET_NULL, null=True)
    # e = models.ForeignKey(SkillModel, related_name='e', on_delete=models.SET_NULL, null=True)
    # r = models.ForeignKey(SkillModel, related_name='r', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

