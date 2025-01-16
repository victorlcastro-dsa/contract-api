import re
from validate_docbr import CNPJ
from email_validator import validate_email, EmailNotValidError

def validate_cnpj(cnpj: str) -> bool:
    """
    Validates the CNPJ by checking its format and logic.

    :param cnpj: The CNPJ to be validated (format XX.XXX.XXX/0001-YY)
    :return: True if the CNPJ is valid, False otherwise.
    """
    # Validate the format using regex
    cnpj_pattern = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
    if not re.match(cnpj_pattern, cnpj):
        return False

    # Validate the logical part of the CNPJ
    cnpj_validator = CNPJ()
    return cnpj_validator.validate(cnpj)

def validate_zip_code(value: str) -> bool:
    """
    Validates the Brazilian CEP (zip code).
    """
    cep_pattern = r'^\d{5}-\d{3}$'
    if not re.match(cep_pattern, value):
        raise ValueError(f"Invalid zip code: {value}")
    return True

def validate_phone_number(phone_number: str) -> bool:
    """
    Validates the phone number to be either a landline or mobile number.
    """
    phone_pattern = r'^\(?\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}$'
    if not re.match(phone_pattern, phone_number):
        raise ValueError(f"Invalid phone number: {phone_number}")
    return True

def validate_email_address(email: str) -> bool:
    """
    Validates the email address.
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        raise ValueError(f"Invalid email address: {email}")