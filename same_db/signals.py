from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from django.db import connection


@receiver(post_save, sender=Post)
def post_saved_handler(sender, instance, created, **kwargs):
    print("Signal received inside post_saved_handler")
    # Check if the transaction is still open
    print(f"Connection in transaction? {connection.in_atomic_block}")
