# Generated by Django 3.1 on 2021-08-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveIntegerField(default=0, verbose_name='Скидка, %'),
        ),
        migrations.AlterField(
            model_name='product',
            name='engine',
            field=models.CharField(choices=[('petrol', 'Бензин'), ('diesel', 'Дизель'), ('electro', 'Электро'), ('hybrid', 'Гибрид'), ('diesel gas', 'Дизель+газ'), ('petrol gas', 'Бензин+газ'), ('gas', 'Газ'), ('not specified', 'Не указано')], default='not specified', max_length=30, verbose_name='Двигатель'),
        ),
        migrations.AlterField(
            model_name='product',
            name='power',
            field=models.PositiveIntegerField(verbose_name='Мощность, л. с.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Автомат'), ('mechanical', 'Механическая'), ('pneumatic', 'Пневматическая'), ('robot', 'Робот'), ('variable', 'Вариатор'), ('not specified', 'Не указано')], default='not specified', max_length=20, verbose_name='Коробка'),
        ),
        migrations.AlterField(
            model_name='product',
            name='year_of_issue',
            field=models.PositiveIntegerField(verbose_name='Год выпуска'),
        ),
    ]
