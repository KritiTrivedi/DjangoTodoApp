# Generated by Django 4.2.5 on 2023-10-04 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimingTodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('timing', models.DateTimeField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.todo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
