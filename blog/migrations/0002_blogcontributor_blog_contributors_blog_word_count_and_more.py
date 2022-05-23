# Generated by Django 4.0.2 on 2022-05-10 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0004_alter_user_follows'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogContributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribution', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='contributors',
            field=models.ManyToManyField(related_name='contributions', through='blog.BlogContributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='word_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogcontributor',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
        migrations.AddField(
            model_name='blogcontributor',
            name='contributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='blogcontributor',
            unique_together={('contributor', 'blog')},
        ),
    ]
