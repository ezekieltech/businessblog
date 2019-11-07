# Generated by Django 2.2.2 on 2019-11-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezekielpost', '0010_post_industry'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='focus',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(blank=True, choices=[('post', 'post'), ('page', 'page'), ('case_studies', 'case_studies')], max_length=400, null=True),
        ),
        migrations.DeleteModel(
            name='Casestudies',
        ),
    ]
