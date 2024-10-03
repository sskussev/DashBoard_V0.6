from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    position = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Должность',
    )
    class Meta:
        permissions = (
            ('vpn_performance', 'vpn performance'),
            ('map', 'map'),
            ('interactive_chart', 'interactive chart'),
            ('access_to_blocked_resources', 'access to blocked resources'),
            ('reports_and_documents', 'reports and documents'),
            ('new_func', 'new function'),
            ('archive', 'archive'),
            ('main_page', 'main page'),
            ('analytics', 'analytics'),
        )
    def __str__(self):
        return self.username
