# Generated by Django 4.1.4 on 2022-12-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonay_loisirs', '0006_classement'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Classement',
        ),
        migrations.AddField(
            model_name='match',
            name='points_equipe_receveuse',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='points_equipe_visiteuse',
            field=models.IntegerField(default=0),
        ),
    ]