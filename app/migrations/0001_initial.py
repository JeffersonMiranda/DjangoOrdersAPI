# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-20 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('precoUnitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rentabilidade', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('precoUnitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('multiplo', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rentabilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pedido'),
        ),
        migrations.AddField(
            model_name='item',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Produto'),
        ),
    ]
