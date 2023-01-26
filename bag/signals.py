from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from shop.models import OrderDesignItem

@receiver(post_save, sender=OrderDesignItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

@receiver(post_delete, sender=OrderDesignItem)
def delete_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem on delete
    """
    instance.order.update_total()