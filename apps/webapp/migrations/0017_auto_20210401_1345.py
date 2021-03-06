# Generated by Django 3.1.7 on 2021-04-01 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_film_starships'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('vehicle_class', models.CharField(blank=True, max_length=40, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=40, null=True)),
                ('length', models.CharField(blank=True, max_length=40, null=True)),
                ('cost_in_credits', models.CharField(blank=True, max_length=40, null=True)),
                ('crew', models.CharField(blank=True, max_length=40, null=True)),
                ('passengers', models.CharField(blank=True, max_length=40, null=True)),
                ('max_atmosphering_speed', models.CharField(blank=True, max_length=40, null=True)),
                ('cargo_capacity', models.CharField(blank=True, max_length=40, null=True)),
                ('consumables', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
                'db_table': 'vehicle',
                'ordering': ['name'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmCharacter',
            fields=[
                ('film_person_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Film Character',
                'verbose_name_plural': 'Film Characters',
                'db_table': 'film_character',
                'ordering': ['film', 'character'],
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'managed': False, 'ordering': ['title'], 'verbose_name': 'Film', 'verbose_name_plural': 'Films'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'managed': False, 'ordering': ['name'], 'verbose_name': 'Person', 'verbose_name_plural': 'Persons'},
        ),
        migrations.AlterModelOptions(
            name='planet',
            options={'managed': False, 'ordering': ['name'], 'verbose_name': 'Planet', 'verbose_name_plural': 'Planets'},
        ),
        migrations.AlterModelOptions(
            name='species',
            options={'managed': False, 'ordering': ['name'], 'verbose_name': 'Species', 'verbose_name_plural': 'Species'},
        ),
        migrations.AlterModelOptions(
            name='starship',
            options={'managed': False, 'ordering': ['name'], 'verbose_name': 'Starship', 'verbose_name_plural': 'Starships'},
        ),
        migrations.AddField(
            model_name='filmcharacter',
            name='character',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.person'),
        ),
        migrations.AddField(
            model_name='filmcharacter',
            name='film',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.film'),
        ),
        migrations.AlterUniqueTogether(
            name='filmcharacter',
            unique_together={('film', 'character')},
        ),
    ]
