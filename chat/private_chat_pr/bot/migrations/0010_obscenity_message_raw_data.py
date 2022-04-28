# Generated by Django 4.0.3 on 2022-03-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_client_keyboard_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obscenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='raw_data',
            field=models.JSONField(default=dict),
        ),
    ]
