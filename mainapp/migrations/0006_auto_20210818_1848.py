# Generated by Django 3.2.5 on 2021-08-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210818_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flower',
            name='diagonal',
        ),
        migrations.RemoveField(
            model_name='flower',
            name='display_type',
        ),
        migrations.RemoveField(
            model_name='flower',
            name='processor_freq',
        ),
        migrations.RemoveField(
            model_name='flower',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='flower',
            name='time_without_charge',
        ),
        migrations.RemoveField(
            model_name='flower',
            name='video',
        ),
        migrations.RemoveField(
            model_name='flowerinpot',
            name='accum_volume',
        ),
        migrations.RemoveField(
            model_name='flowerinpot',
            name='diagonal',
        ),
        migrations.RemoveField(
            model_name='flowerinpot',
            name='display_type',
        ),
        migrations.RemoveField(
            model_name='flowerinpot',
            name='frontal_cam_mp',
        ),
        migrations.RemoveField(
            model_name='flowerinpot',
            name='main_cam_mp',
        ),
        migrations.RemoveField(
            model_name='flowerinpot',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='flowerinpot',
            name='resolution',
        ),
        migrations.RemoveField(
            model_name='flowerinpot',
            name='sd',
        ),
        migrations.RemoveField(
            model_name='flowerinpot',
            name='sd_volume_max',
        ),
        migrations.AddField(
            model_name='flower',
            name='country',
            field=models.CharField(default='default title', max_length=255, verbose_name='Страна'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flower',
            name='history',
            field=models.CharField(default='default title', max_length=255, verbose_name='История'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flower',
            name='scent',
            field=models.CharField(default='default title', max_length=255, verbose_name='Аромат'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flower',
            name='variety',
            field=models.CharField(default='default title', max_length=255, verbose_name='Сорт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flowerinpot',
            name='country',
            field=models.CharField(default='default title', max_length=255, verbose_name='Страна'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flowerinpot',
            name='flower_pot',
            field=models.CharField(default='default title', max_length=255, verbose_name='Цветочный горшок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flowerinpot',
            name='history',
            field=models.CharField(default='default title', max_length=255, verbose_name='История'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flowerinpot',
            name='scent',
            field=models.CharField(default='default title', max_length=255, verbose_name='Аромат'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flowerinpot',
            name='variety',
            field=models.CharField(default='default title', max_length=255, verbose_name='Сорт'),
            preserve_default=False,
        ),
    ]
