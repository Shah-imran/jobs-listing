# Generated by Django 3.1 on 2021-08-04 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_post', '0003_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostViewMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip', models.GenericIPAddressField(default='')),
                ('views', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_post.post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
