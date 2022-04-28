# Generated by Django 4.0.3 on 2022-03-22 19:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_alter_client_hash_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='hash_link',
        ),
        migrations.AddField(
            model_name='client',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
