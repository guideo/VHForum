# Generated by Django 2.0 on 2017-12-26 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20171223_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsection',
            name='subsection_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Section'),
        ),
    ]