from django.db import models

import uuid


class Skill(models.Model):
    class Meta:
        unique_together = ('patch', 'name')

    skill_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=32)

    patch = models.FloatField(default=0)

    base_damage = models.IntegerField(default=0)
    ad_ratio = models.FloatField(default=0)
    ap_ratio = models.FloatField(default=0)
    base_damage_growth = models.IntegerField(default=0)
    ad_ratio_growth = models.FloatField(default=0)
    ap_ratio_growth = models.FloatField(default=0)

    description = models.TextField()

    def __str__(self):
        return self.name


class Champion(models.Model):
    class Meta:
        unique_together = ('patch', 'name')

    champion_id = models.AutoField(primary_key=True, editable=False)

    name = models.CharField(max_length=16, null=False)
    japanese_name = models.CharField(max_length=16, null=False)

    patch = models.FloatField(default=0)

    health = models.FloatField(default=0)
    health_growth = models.FloatField(default=0)
    health_regen = models.FloatField(default=0)
    health_regen_growth = models.FloatField(default=0)

    resource_name = models.CharField(max_length=16, null=False, default="undefined")
    resource = models.FloatField(default=0)
    resource_growth = models.FloatField(default=0)
    resource_regen = models.FloatField(default=0)
    resource_regen_growth = models.FloatField(default=0)

    range = models.FloatField(default=0)
    attack_damage = models.FloatField(default=0)
    attack_damage_growth = models.FloatField(default=0)
    attack_speed = models.FloatField(default=0)
    attack_speed_growth = models.FloatField(default=0)

    armor = models.IntegerField(default=0)
    armor_growth = models.FloatField(default=0)
    magic_resist = models.FloatField(default=0)
    magic_resist_growth = models.FloatField(default=0)
    move_speed = models.FloatField(default=0)

    passive = models.ForeignKey(Skill, related_name='passive', on_delete=models.SET_NULL, null=True)
    q = models.ForeignKey(Skill, related_name='q', on_delete=models.SET_NULL, null=True)
    w = models.ForeignKey(Skill, related_name='w', on_delete=models.SET_NULL, null=True)
    e = models.ForeignKey(Skill, related_name='e', on_delete=models.SET_NULL, null=True)
    r = models.ForeignKey(Skill, related_name='r', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

