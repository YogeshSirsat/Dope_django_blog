# Generated by Django 3.0.5 on 2020-04-26 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dope_blog', '0005_auto_20200426_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heading',
            name='Post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='headings', to='Dope_blog.Posts'),
        ),
    ]
