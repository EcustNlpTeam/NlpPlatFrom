# Generated by Django 3.0.2 on 2020-02-14 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30)),
                ('pass_word', models.CharField(max_length=64)),
                ('user_token', models.CharField(max_length=64)),
                ('token_last_modified', models.DateTimeField()),
            ],
        ),
    ]
