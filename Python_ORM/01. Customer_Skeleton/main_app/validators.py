from django.core.exceptions import ValidationError


def check_name(value):
    for c in value:
        if not c.isalpha or not c.isspace:
            raise ValidationError("Name can only contain letters and spaces")
