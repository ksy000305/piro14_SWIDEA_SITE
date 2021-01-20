# Generated by Django 2.0.13 on 2021-01-20 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210120_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devtool',
            name='desc',
            field=models.TextField(blank=True, verbose_name='>> 개발툴 설명'),
        ),
        migrations.AlterField(
            model_name='devtool',
            name='kind',
            field=models.CharField(max_length=100, verbose_name='>> 종류'),
        ),
        migrations.AlterField(
            model_name='devtool',
            name='name',
            field=models.CharField(max_length=100, verbose_name='>> 이름'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='content',
            field=models.TextField(blank=True, verbose_name='>> 아이디어 설명'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='devtool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Devtool'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='image',
            field=models.ImageField(upload_to='idea_main_image', verbose_name='>> 대표 사진'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='interest',
            field=models.IntegerField(default=0, verbose_name='>> 아이디어 관심도'),
        ),
        migrations.AlterField(
            model_name='idea',
            name='title',
            field=models.CharField(max_length=100, verbose_name='>> 아이디어명'),
        ),
    ]
