from django.core.exceptions import ValidationError

def validate_iban(value):
    if not str(value).startswith('TR') and len(value) != 16:
        raise ValidationError(
            'IBAN number is incorrect'
        )