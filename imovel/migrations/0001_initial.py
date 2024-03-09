# Generated by Django 5.0.3 on 2024-03-09 13:38

import django.db.models.deletion
import shortuuid.main
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_imovel', models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=22, unique=True)),
                ('limite_hospedes', models.IntegerField(blank=True, default=None, null=True)),
                ('qtd_banheiro', models.IntegerField(blank=True, default=None, null=True)),
                ('aceita_animais', models.BooleanField(default=False)),
                ('valor_limpeza', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_ativacao', models.DateField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalImovel',
            fields=[
                ('history_id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('codigo_imovel', models.CharField(db_index=True, default=shortuuid.main.ShortUUID.uuid, max_length=22)),
                ('limite_hospedes', models.IntegerField(blank=True, default=None, null=True)),
                ('qtd_banheiro', models.IntegerField(blank=True, default=None, null=True)),
                ('aceita_animais', models.BooleanField(default=False)),
                ('valor_limpeza', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_ativacao', models.DateField()),
                ('criado_em', models.DateTimeField(blank=True, editable=False)),
                ('ultima_atualizacao', models.DateTimeField(blank=True, editable=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_relation', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='historic', to='imovel.imovel')),
            ],
            options={
                'verbose_name': 'historical imovel',
                'verbose_name_plural': 'historical imovels',
                'db_table': 'imovel_historico',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
