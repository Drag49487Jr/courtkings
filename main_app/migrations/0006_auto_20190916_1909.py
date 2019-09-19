# Generated by Django 2.2.3 on 2019-09-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20190916_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='assist_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='block_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='nba_team',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='point_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='rebound_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='steal_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='threepointer_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='turnover_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='losses',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='points',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wins',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_assists',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_blocks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_rebounds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_steals',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_threepointers',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_turnovers',
            field=models.IntegerField(null=True),
        ),
    ]
