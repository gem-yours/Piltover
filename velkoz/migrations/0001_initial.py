# Generated by Django 2.2.1 on 2019-09-11 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('skill_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('patch', models.FloatField(default=0)),
                ('base_damage', models.IntegerField(default=0)),
                ('ad_ratio', models.FloatField(default=0)),
                ('ap_ratio', models.FloatField(default=0)),
                ('base_damage_growth', models.IntegerField(default=0)),
                ('ad_ratio_growth', models.FloatField(default=0)),
                ('ap_ratio_growth', models.FloatField(default=0)),
                ('description', models.TextField()),
            ],
            options={
                'unique_together': {('patch', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('champion_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16)),
                ('japanese_name', models.CharField(max_length=16)),
                ('patch', models.FloatField(default=0)),
                ('health', models.FloatField(default=0)),
                ('health_growth', models.FloatField(default=0)),
                ('health_regen', models.FloatField(default=0)),
                ('health_regen_growth', models.FloatField(default=0)),
                ('resource_name', models.CharField(default='undefined', max_length=16)),
                ('resource', models.FloatField(default=0)),
                ('resource_growth', models.FloatField(default=0)),
                ('resource_regen', models.FloatField(default=0)),
                ('resource_regen_growth', models.FloatField(default=0)),
                ('range', models.FloatField(default=0)),
                ('attack_damage', models.FloatField(default=0)),
                ('attack_damage_growth', models.FloatField(default=0)),
                ('attack_speed', models.FloatField(default=0)),
                ('attack_speed_growth', models.FloatField(default=0)),
                ('armor', models.IntegerField(default=0)),
                ('armor_growth', models.FloatField(default=0)),
                ('magic_resist', models.FloatField(default=0)),
                ('magic_resist_growth', models.FloatField(default=0)),
                ('move_speed', models.FloatField(default=0)),
                ('e', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='e', to='velkoz.Skill')),
                ('passive', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passive', to='velkoz.Skill')),
                ('q', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='q', to='velkoz.Skill')),
                ('r', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='r', to='velkoz.Skill')),
                ('w', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='w', to='velkoz.Skill')),
            ],
            options={
                'unique_together': {('patch', 'name')},
            },
        ),
    ]
