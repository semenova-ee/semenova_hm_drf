from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

DISALLOWED_DOMAINS = [
    'linkedin.com',
    'tumblr.com',
    'tilda.cc',
    'wordpress.com',
]

def validate_allowed_domains(value):
    for domain in DISALLOWED_DOMAINS:
        if domain in value:
            raise ValidationError(
                _(f'Links to {domain} are not allowed.'),
                params={'value': value},
            )
