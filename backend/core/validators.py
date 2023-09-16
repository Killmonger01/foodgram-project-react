import re

from django.core.exceptions import ValidationError

LEGAL_CHARACTERS_ERROR = (
    "Нельзя использовать символ(ы): " "{forbidden_chars} в имени пользователя."
)
FORBIDDEN_NAMES_ERROR = "Имя пользователя не может быть {value}"


def validate_username(value):
    if value in ("me",):
        raise ValidationError(FORBIDDEN_NAMES_ERROR.format(value=value))
    forbidden_chars = "".join(set(re.compile(r"[\w.@+-]").sub("", value)))
    if forbidden_chars:
        raise ValidationError(
            LEGAL_CHARACTERS_ERROR.format(forbidden_chars=forbidden_chars)
        )
