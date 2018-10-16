# Generated by Django 2.1.2 on 2018-10-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(default='')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
    ]
