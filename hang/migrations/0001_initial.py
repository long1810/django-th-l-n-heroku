# Generated by Django 3.2.7 on 2021-11-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mah', models.CharField(max_length=100)),
                ('ten', models.TextField()),
                ('ngaynhap', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('gia', models.IntegerField()),
                ('so', models.IntegerField()),
            ],
        ),
    ]
