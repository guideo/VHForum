# Generated by Django 2.0 on 2017-12-27 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20171227_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(default='media/users/default/default_img.jpg', upload_to='media/users/images/'),
        ),
    ]
