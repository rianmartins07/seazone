# Generated by Django 5.0.3 on 2024-03-09 13:38

import django.db.models.deletion
import shortuuid.main
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anuncio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_reserva', models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=22, unique=True)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comentario', models.TextField(blank=True, max_length=512, null=True)),
                ('qtd_hospedes', models.IntegerField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('anuncio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anuncio.anuncio')),
            ],
            options={
                'db_table': 'reserva',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HistoricalReserva',
            fields=[
                ('history_id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('codigo_reserva', models.CharField(db_index=True, default=shortuuid.main.ShortUUID.uuid, max_length=22)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comentario', models.TextField(blank=True, max_length=512, null=True)),
                ('qtd_hospedes', models.IntegerField()),
                ('criado_em', models.DateTimeField(blank=True, editable=False)),
                ('ultima_atualizacao', models.DateTimeField(blank=True, editable=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('anuncio', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='anuncio.anuncio')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_relation', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='historic', to='reserva.reserva')),
            ],
            options={
                'verbose_name': 'historical reserva',
                'verbose_name_plural': 'historical reservas',
                'db_table': 'reserva_historic',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
