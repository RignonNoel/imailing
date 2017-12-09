from .Mailing import IMailing

import sendgrid
from sendgrid.helpers.mail import Email, Content, \
    Substitution, Mail, Personalization

try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib


class Sendgrid(IMailing):

    def __init__(self, api_key):
        super(Sendgrid, self).__init__(api_key)

        self.sg = sendgrid.SendGridAPIClient(
            apikey=self.api_key
        )

    def send_templated_email(self, template_id, email_from,
                             list_to, context=None):

        mail = Mail()
        mail.from_email = Email(email_from, email_from)
        mail.template_id = template_id

        # We need to add a personalization for each user
        for email_to in list_to:
            personalization = Personalization()

            personalization.add_to(Email(email_to, email_to))

            if context:
                for variable in context:
                    personalization.add_substitution(
                        Substitution(variable, context[variable])
                    )

            mail.add_personalization(personalization)

        return self.sg.client.mail.send.post(request_body=mail.get())
