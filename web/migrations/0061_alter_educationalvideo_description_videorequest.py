# Generated by Django 5.1.6 on 2025-04-25 18:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0060_question_choice_response_survey_question_survey"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="educationalvideo",
            name="description",
            field=models.TextField(blank=True, help_text="Optional - describe what viewers will learn from this video"),
        ),
        migrations.CreateModel(
            name="VideoRequest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(help_text="Short title describing the requested video", max_length=200)),
                (
                    "description",
                    models.TextField(help_text="Detailed description of what you'd like to learn from this video"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("approved", "Approved"),
                            ("fulfilled", "Fulfilled"),
                            ("rejected", "Rejected"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="video_requests", to="web.subject"
                    ),
                ),
                (
                    "fulfilled_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="Educational video that fulfills this request",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="fulfilling_requests",
                        to="web.educationalvideo",
                    ),
                ),
                (
                    "requester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="video_requests",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Video Request",
                "verbose_name_plural": "Video Requests",
                "ordering": ["-created_at"],
            },
        ),
    ]
