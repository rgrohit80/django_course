from django.db.models.signals import post_delete
from .models import Page
from django.dispatch import receiver


@receiver(post_delete, sender=Page)
def delete_related_user(sender, instance, **kwargs):
    print("page post delete")
    instance.user.delete()
