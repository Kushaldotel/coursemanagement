from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from account.models import StudentUser

@receiver(post_save, sender=StudentUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        password = getattr(instance, "_raw_password", "Password not available")

        email_subject = "Welcome to Course Management System!"
        email_body = f"""
        Hello {instance.first_name},

        Welcome to our course management system!
        Your login credentials are:

        Email: {instance.email}
        Password: {password}

        Please log in and start your journey!

        Best Regards,
        Course Management Team
        """

        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )
