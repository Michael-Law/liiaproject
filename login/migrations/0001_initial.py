# Generated by Django 3.0.1 on 2020-01-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(default='foobar', max_length=200)),
                ('teamlogin', models.CharField(default='foobar', max_length=200)),
                ('teampassword', models.TextField(default='foobar', max_length=200)),
            ],
        ),
    ]
