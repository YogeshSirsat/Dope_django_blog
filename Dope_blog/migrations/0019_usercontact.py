# Generated by Django 3.0.5 on 2020-04-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dope_blog', '0018_post_markdown'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usercontact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('query', models.TextField(max_length=500)),
            ],
        ),
    ]
