# Generated by Django 4.1.2 on 2022-10-11 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_remove_jobdescrip_categorys'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdescrip',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='web.categories'),
            preserve_default=False,
        ),
    ]