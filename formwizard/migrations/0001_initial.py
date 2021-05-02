# Generated by Django 3.2 on 2021-05-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('password_comfirm', models.CharField(max_length=100)),
                ('education_level', models.CharField(choices=[('Primary Level', 'Primary Level'), ('Form Six', 'Form Six'), ('University Level', 'University Level')], max_length=100)),
            ],
        ),
    ]