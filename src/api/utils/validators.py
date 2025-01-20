import re
from validate_docbr import CNPJ
from email_validator import validate_email, EmailNotValidError

def validate_cnpj(cnpj: str) -> bool:
    """
    Validates the CNPJ by checking its format and logic.

    :param cnpj: The CNPJ to be validated (format XX.XXX.XXX/0001-YY)
    :return: True if the CNPJ is valid, False otherwise.
    """
    try:
        # Validate the format using regex
        cnpj_pattern = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
        if not re.match(cnpj_pattern, cnpj):
            return False

        # Validate the logical part of the CNPJ
        cnpj_validator = CNPJ()
        if not cnpj_validator.validate(cnpj):
            return False

        return True
    except Exception:
        return False

def validate_zip_code(value: str) -> bool:
    """
    Validates the Brazilian CEP (zip code).

    :return: True if the zip code is valid, False otherwise.
    """
    try:
        cep_pattern = r'^\d{5}-\d{3}$'
        if not re.match(cep_pattern, value):
            return False

        return True
    except Exception:
        return False

def validate_phone_number(phone_number: str) -> bool:
    """
    Validates the phone number to be either a landline or mobile number.

    :return: True if the phone number is valid, False otherwise.
    """
    try:
        phone_pattern = r'^\(?\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}$'
        if not re.match(phone_pattern, phone_number):
            return False

        return True
    except Exception:
        return False

def validate_email_address(email: str) -> bool:
    """
    Validates the email address.

    :return: True if the email address is valid, False otherwise.
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False
    except Exception:
        return False