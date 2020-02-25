# Generated by Django 3.0.3 on 2020-02-25 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AcaiFake',
        ),
        migrations.AddField(
            model_name='pedido',
            name='resumo',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Acai'),
        ),
    ]