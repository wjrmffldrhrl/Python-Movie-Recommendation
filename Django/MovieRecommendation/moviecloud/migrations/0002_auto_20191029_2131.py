# Generated by Django 2.2.6 on 2019-10-29 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviecloud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='wordcloud',
            field=models.URLField(max_length=100, verbose_name='wordcloud 이미지 경로'),
        ),
    ]