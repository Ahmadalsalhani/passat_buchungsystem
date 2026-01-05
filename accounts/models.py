from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Erweitertes User-Model mit Rollen
    """
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('user', 'Benutzer'),
    )
    
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='Rolle'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Aktualisiert am')
    
    class Meta:
        verbose_name = 'Benutzer'
        verbose_name_plural = 'Benutzer'
        ordering = ['username']
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    def is_admin_role(self):
        """Prüft ob der Benutzer Admin-Rolle hat"""
        return self.role == 'admin' or self.is_superuser
