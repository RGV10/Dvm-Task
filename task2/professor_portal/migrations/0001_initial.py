# Generated by Django 5.0.4 on 2024-04-13 14:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_portal', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('attachment', models.FileField(blank=True, upload_to='announcements/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_portal.course')),
            ],
        ),
        migrations.CreateModel(
            name='Evals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.FileField(blank=True, upload_to='announcements/')),
                ('marks', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_portal.course')),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_portal.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_portal.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]