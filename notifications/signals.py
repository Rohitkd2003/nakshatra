# notifications/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Notification

@receiver(post_save, sender=Notification)
def send_email_notification(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject=instance.title,
            message=instance.message,
            from_email='your_email@gmail.com',
            recipient_list=[instance.user.email],
            fail_silently=True,
        )
