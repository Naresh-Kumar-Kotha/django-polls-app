# Generated by Django 3.2 on 2021-12-15 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('polls', '0002_alter_question_question_text'),]

    operations = [migrations.AlterField(model_name='question',name='question_text',field=models.CharField(max_length=200),),]
