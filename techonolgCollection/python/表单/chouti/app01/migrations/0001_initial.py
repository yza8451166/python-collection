# Generated by Django 2.0.1 on 2018-02-06 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SendMsg',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=6)),
                ('email', models.EmailField(db_index=True, max_length=32)),
                ('times', models.IntegerField(default=0, max_length=2)),
                ('ctime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=32, unique=True)),
                ('ctime', models.DateTimeField()),
            ],
        ),
    ]
