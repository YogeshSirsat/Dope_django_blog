# Generated by Django 3.0.5 on 2020-05-17 17:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dope_blog', '0043_auto_20200515_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='markdown',
        ),
        migrations.AlterField(
            model_name='heading',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='subheading',
            name='subtext',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=5000, null=True),
        ),
    ]
