from .Mailing import IMailing
from mailin import Mailin


class SendinBlue(IMailing):

    def __init__(self, api_key):
        super(SendinBlue, self).__init__(api_key)

        self.mailin = Mailin(
            "https://api.sendinblue.com/v2.0",
            self.api_key,
        )

    def send_templated_email(self, template_id,
                             email_from, list_to, context=None):
        # Initial data
        data = {
            "id": template_id,
            "attr": {},
            "to": list_to[0],
            "headers": {
                "Content-Type": "text/html;charset=iso-8859-1",
            }
        }

        # Add context in data
        if context:
            for variable in context:
                data['attr'][variable] = context[variable]

        # Connection to API
        result = self.mailin.send_transactional_template(data)
        return result
