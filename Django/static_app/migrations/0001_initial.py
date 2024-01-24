# Generated by Django 4.2.8 on 2023-12-19 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("music_rec_app", "0004_rename_playback_playlisttrack_cnt"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="user_track_agg",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(blank=True, max_length=30, null=True)),
                ("track", models.CharField(max_length=200)),
                ("cnt", models.IntegerField(blank=True, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "track_id",
                    models.ForeignKey(
                        blank=True,
                        db_column="TRACK_ID",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="music_rec_app.track",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        db_column="USER_ID",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "USER_TRACK_AGG",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="user_day_agg",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(blank=True, max_length=30, null=True)),
                ("day_of_week", models.CharField(blank=True, max_length=30, null=True)),
                ("cnt", models.IntegerField(blank=True, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        db_column="USER_ID",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "USER_DAY_AGG",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="user_artist_agg",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(blank=True, max_length=30, null=True)),
                ("artist", models.CharField(max_length=200)),
                ("cnt", models.IntegerField(blank=True, null=True)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "artist_id",
                    models.ForeignKey(
                        blank=True,
                        db_column="ARTIST_ID",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="music_rec_app.artist",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        db_column="USER_ID",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "USER_ARTIST_AGG",
                "managed": True,
            },
        ),
    ]