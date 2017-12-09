=====
Usage
=====

To use IMailing in a project::

    from imailing.Mailing import IMailing

    # Create a new instance
    email = IMailing.create_instance(
    'SendinBlue',  # or `SendinBlue`
    'YOUR_API_KEY'
    )

    # Send an email
    response_send_mail = email.send_templated_email(
        email_from='admin@mydomain.com',
        template_id='1',
        list_to=['user@hisdomain.com'],
        context={
            "name": 'Thierry',
            "url_button": 'https://mysite.com/',
        },
    )

    # Check the result of your request
    print(response_send_mail)
