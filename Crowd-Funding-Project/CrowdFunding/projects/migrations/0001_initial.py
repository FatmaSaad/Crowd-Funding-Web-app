# Generated by Django 3.0.4 on 2020-03-20 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('tags', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_title', models.CharField(max_length=100)),
                ('project_details', models.TextField(default=' ')),
                ('project_hint', models.TextField(default=' ')),
                ('project_Location', models.CharField(max_length=500)),
                ('total_donation', models.IntegerField()),
                ('donated', models.IntegerField(default=0)),
                ('Percentage', models.IntegerField(default=0)),
                ('rate', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('main_img_name', models.TextField(default=' ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Categories')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
        ),
    ]
