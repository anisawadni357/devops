# Generated by Django 4.0.2 on 2022-04-28 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Crrefourplatforme', '0007_remove_camion_enpanne_camion_fonctionnelle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listelivraisonsec',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Crrefourplatforme.markets'),
        ),
    ]