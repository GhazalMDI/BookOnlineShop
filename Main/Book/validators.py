from django.core.exceptions import ValidationError


def validatedPrice(price):
    if price > 5000:
        raise ValidationError('لطفا قیمت کتاب را صحیح وارد نمایید')
    raise price



