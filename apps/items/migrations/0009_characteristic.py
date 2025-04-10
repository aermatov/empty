# Generated by Django 5.1.7 on 2025-03-16 18:36

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_alter_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст характеристики')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='characteristic', to='items.item')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристика',
            },
        ),
    ]
