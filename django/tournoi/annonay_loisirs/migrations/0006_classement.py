# Generated by Django 4.1.4 on 2022-12-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonay_loisirs', '0005_alter_match_aller_ou_retour_alter_match_résultat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_equipe_receveuse', models.IntegerField(null=True, verbose_name='Points gagnés')),
                ('points_equipe_visiteuse', models.IntegerField(null=True, verbose_name='Points gagnés')),
            ],
        ),
    ]
