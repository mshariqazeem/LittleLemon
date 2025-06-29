# Generated by Django 5.2 on 2025-06-23 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_booking_comment_remove_booking_guest_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='reservation_slot',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='menu_item_description',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='name',
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='Guest', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='reservation_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
