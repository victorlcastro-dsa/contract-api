import re
from validate_docbr import CNPJ

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