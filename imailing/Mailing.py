# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class IMailing:
    """
    This interface allow us to manage transactionnal
    email from multiple services with a standardized
    interface.
    """
    __metaclass__ = ABCMeta

    def __init__(self, api_key):
        self.api_key = api_key

    @staticmethod
    def create_instance(service, api_key):
        if service == "SendinBlue":
            from .SendinBlue import SendinBlue
            return SendinBlue(api_key)
        elif service == "Sendgrid":
            from .Sendgrid import Sendgrid
            return Sendgrid(api_key)
        else:
            raise ValueError('Service "{0}" is not supported.'.format(service))

    @abstractmethod
    def send_templated_email(self, template_id, email_from,
                             list_to, list_cc, list_bcc, context):
        """
        Method to send a transactional email
        :param template_id: Id of the template in your service
        :param email_from: Email of the sender
        :param list_to: List of email address to send
        :param list_cc: List of email address to send in cc
        :param list_bcc: List of email address to send in bcc
        :param context: Dictionary of context for variable
        :return:
        """
        raise NotImplementedError
