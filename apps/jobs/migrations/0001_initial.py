# Generated by Django 4.2.2 on 2023-09-09 08:01

import django.db.models.deletion
from django.db import migrations, models

import apps.jobs.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("name", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("about", models.TextField(default=None, max_length=500)),
                (
                    "company_id",
                    models.UUIDField(
                        default=apps.jobs.models.hex_uuid,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
            options={
                "db_table": "tbl_company",
            },
        ),
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "job_id",
                    models.UUIDField(
                        default=apps.jobs.models.hex_uuid,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("job_role", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(default="No description provided", max_length=500),
                ),
                ("location", models.CharField(default=None, max_length=100)),
                ("post_date", models.DateField()),
                ("posted", models.BooleanField(default=False)),
                ("experience", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="companyies",
                        to="jobs.company",
                    ),
                ),
            ],
            options={
                "db_table": "tbl_job",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "user_id",
                    models.UUIDField(
                        default=apps.jobs.models.hex_uuid,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
                ("address", models.TextField(max_length=100)),
                ("phone", models.CharField(default=None, max_length=12, null=True)),
                ("about", models.TextField(default=None, max_length=100)),
                ("resume", models.FileField(null=True, upload_to="resume/")),
                (
                    "profile_picture",
                    models.FileField(null=True, upload_to="profile_picture/"),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.company"
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobs.job"
                    ),
                ),
            ],
            options={
                "db_table": "tbl_user_profile",
            },
        ),
    ]
