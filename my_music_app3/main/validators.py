from django.core.exceptions import ValidationError


def validate_if_username_contains_letters_numbers_and_underscores(username):
    if not all([ch.isalpha() or ch.isdigit() or ch == '_' for ch in username]):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
    return None


