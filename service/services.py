from django.core.mail import send_mail
from django.utils import timezone
from my_project.settings import EMAIL_HOST_USER
from service.models import Mailing, Attempt


def is_started():
    now_time = timezone.now()
    letters = Mailing.objects.filter(date_time_send__lte=now_time, status='created')
    for letter in letters:
        letter.status = 'started'
        letter.save()


def daily(*args):
    letters = Mailing.objects.filter(periodicity='daily', status='started')
    for letter in letters:

        try:

            client_list = letter.clients
            for client in client_list:
                send_mail(client, 'new letter', from_email=EMAIL_HOST_USER, recipient_list=[client.email])
                Attempt.objects.create(date_time_attempt=timezone.now(), status='success', send_mail=letter)
        except Exception as e:
            Attempt.objects.create(date_time_attempt=timezone.now(), status='failed', send_mail=letter,
                                       response_from_mail_server=str(e))

def weekly(*args):
    letters = Mailing.objects.filter(periodicity='weekly', status='started')
    for letter in letters:
        client_list = letter.clients
        for client in client_list:
            send_mail(client, 'new letter', from_email=EMAIL_HOST_USER, recipient_list=[client.email])

def monthly(*args):
    letters = Mailing.objects.filter(periodicity='monthly', status='started')
    for letter in letters:
        client_list = letter.clients
        for client in client_list:
            send_mail(client, 'new letter', from_email=EMAIL_HOST_USER, recipient_list=[client.email])