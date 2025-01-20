import re
from validate_docbr import CNPJ
from email_validator import validate_email, EmailNotValidError
from .response import ResponseHandler

def validate_cnpj(cnpj: str):
    """
    Validates the CNPJ by checking its format and logic.

    :param cnpj: The CNPJ to be validated (format XX.XXX.XXX/0001-YY)
    :return: ResponseHandler.success if the CNPJ is valid, ResponseHandler.error otherwise.
    """
    try:
        # Validate the format using regex
        cnpj_pattern = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
        if not re.match(cnpj_pattern, cnpj):
            return ResponseHandler.error(message=f"Invalid CNPJ format: {cnpj}")

        # Validate the logical part of the CNPJ
        cnpj_validator = CNPJ()
        if not cnpj_validator.validate(cnpj):
            return ResponseHandler.error(message=f"Invalid CNPJ: {cnpj}")

        return ResponseHandler.success(message="CNPJ is valid")
    except Exception as e:
        return ResponseHandler.exception(e)

def validate_zip_code(value: str):
    """
    Validates the Brazilian CEP (zip code).

    :return: ResponseHandler.success if the zip code is valid, ResponseHandler.error otherwise.
    """
    try:
        cep_pattern = r'^\d{5}-\d{3}$'
        if not re.match(cep_pattern, value):
            return ResponseHandler.error(message=f"Invalid zip code: {value}")

        return ResponseHandler.success(message="Zip code is valid")
    except Exception as e:
        return ResponseHandler.exception(e)

def validate_phone_number(phone_number: str):
    """
    Validates the phone number to be either a landline or mobile number.

    :return: ResponseHandler.success if the phone number is valid, ResponseHandler.error otherwise.
    """
    try:
        phone_pattern = r'^\(?\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}$'
        if not re.match(phone_pattern, phone_number):
            return ResponseHandler.error(message=f"Invalid phone number: {phone_number}")

        return ResponseHandler.success(message="Phone number is valid")
    except Exception as e:
        return ResponseHandler.exception(e)

def validate_email_address(email: str):
    """
    Validates the email address.

    :return: ResponseHandler.success if the email address is valid, ResponseHandler.error otherwise.
    """
    try:
        validate_email(email)
        return ResponseHandler.success(message="Email address is valid")
    except EmailNotValidError as e:
        return ResponseHandler.error(message=f"Invalid email address: {email}")
    except Exception as e:
        return ResponseHandler.exception(e)