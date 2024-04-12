from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

ALLOWED_DOMAINS = [
    'youtube.com',
]

def validate_allowed_domains(value):
    for domain in ALLOWED_DOMAINS:
        if value != domain:
            raise ValidationError(
                _(f'Links to {domain} are not allowed.'),
                params={'value': value},
            )
