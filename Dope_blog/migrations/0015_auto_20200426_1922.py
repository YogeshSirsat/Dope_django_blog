# Generated by Django 3.0.5 on 2020-04-26 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dope_blog', '0014_heading_subheading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='heading',
            name='subheading',
        ),
        migrations.AddField(
            model_name='heading',
            name='subheading',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='headings', to='Dope_blog.Subheading'),
        ),
    ]
