# Generated by Django 5.0.1 on 2024-02-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TaskCategory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('assign_date', models.DateField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='TaskCategory.category')),
            ],
        ),
    ]