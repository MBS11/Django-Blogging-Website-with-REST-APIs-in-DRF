# Generated by Django 3.1.6 on 2021-03-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210305_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Article', '1'), ('Poem', '2')], default='1', max_length=14),
        ),
    ]
