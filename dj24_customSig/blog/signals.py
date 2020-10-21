from django.dispatch import Signal, receiver
from django.contrib.auth.models import User

# creating signal

notification = Signal(providing_args=["request", "user", "name"])


# Receiver function
@receiver(notification)
def show_notification(sender, **kwargs):
    print("sender:", sender)
    print(f'{kwargs}')
    print("Notification")
