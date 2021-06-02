# Generated by Django 3.1.1 on 2020-12-04 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=30)),
                ('article', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]