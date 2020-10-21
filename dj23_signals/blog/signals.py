from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_init, pre_delete, post_init, post_save, post_delete
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('-----------------------')
    print("Logged signals ...run intro..")
    print("sender: ", sender)
    print("Request:", request)
    print("User: ", user)
    print("pass:", user.password)
    print(f'Kwargs:{kwargs}')


@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print('-----------------------')
    print("Logged signals ...run Outro..")
    print("sender: ", sender)
    print("Request:", request)
    print("User: ", user)
    print("pass:", user.password)
    print(f'Kwargs:{kwargs}')


@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print('-----------------------')
    print("Login failed signals .....")
    print("sender: ", sender)
    print("Request:", request)
    print("Credentials: ", credentials)
    print(f'Kwargs:{kwargs}')


@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print('-----------------------')
    print("Pre save signals .....")
    print("sender: ", sender)
    print("Instance:", instance)
    print(f'Kwargs:{kwargs}')


@receiver(post_save, sender=User)
def after_save(sender, instance, created, **kwargs):
    if created:
        print('-----------------------')
        print("new record")
        print("Post save signals .....")
        print("sender: ", sender)
        print("Instance:", instance)
        print(f'Kwargs:{kwargs}')
        print("create:", created)
    else:
        print('-----------------------')
        print("updated")
        print("Post save signals .....")
        print("sender: ", sender)
        print("Instance:", instance)
        print(f'Kwargs:{kwargs}')
        print("create:", created)


@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print('-----------------------')
    print("at beginning request")
    print('Sender:', sender)
    print('Environ:', environ)
    print(f'Kwargs:{kwargs}')


@receiver(request_finished)
def at_beginning_request(sender, environ, **kwargs):
    print('-----------------------')
    print("at Enging request")
    print('Sender:', sender)
    print('Environ:', environ)
    print(f'Kwargs:{kwargs}')


@receiver(got_request_exception)
def at_beginning_request(sender, environ, **kwargs):
    print('-----------------------')
    print("at Request exception request")
    print('Sender:', sender)
    print('Environ:', environ)
    print(f'Kwargs:{kwargs}')


@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print('--------------------------')
    print("Initial connection to database")
    print("sender:", sender)
    print("Connection:", connection)
    print(f'kwargs:{kwargs}')
