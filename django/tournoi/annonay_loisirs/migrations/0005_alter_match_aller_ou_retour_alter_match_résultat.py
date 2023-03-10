# Generated by Django 4.1.4 on 2022-12-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonay_loisirs', '0004_match_aller_ou_retour_match_résultat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='aller_ou_retour',
            field=models.CharField(choices=[('Match aller', 'Match aller'), ('Match retour', 'Match retour')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='résultat',
            field=models.CharField(choices=[('--', '--'), ('gagné', 'Gagné'), ('nul', 'Nul'), ('perdu', 'Perdu')], default=None, max_length=50, null=True, verbose_name='résultat locaux'),
        ),
    ]
