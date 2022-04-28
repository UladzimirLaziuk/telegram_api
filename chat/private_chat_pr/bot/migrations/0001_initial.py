# Generated by Django 4.0.3 on 2022-03-12 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('ID_CRM', models.CharField(max_length=200, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('tg_chat_id', models.PositiveIntegerField(unique=True)),
                ('tg_user_id', models.PositiveIntegerField(unique=True)),
                ('hash_link', models.PositiveIntegerField(unique=True)),
                ('chats', models.ManyToManyField(related_name='clients', to='bot.chat')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_msg_id', models.PositiveIntegerField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('text', models.TextField(max_length=4096)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.chat')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.client')),
            ],
        ),
    ]