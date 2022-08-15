# Generated by Django 4.0.5 on 2022-08-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('description', models.TextField()),
                ('author', models.IntegerField()),
                ('username', models.CharField(max_length=17)),
            ],
        ),
    ]