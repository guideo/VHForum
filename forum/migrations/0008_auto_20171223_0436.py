# Generated by Django 2.0 on 2017-12-23 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20171222_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subsection',
            name='subsection_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsections', to='forum.Section'),
        ),
    ]