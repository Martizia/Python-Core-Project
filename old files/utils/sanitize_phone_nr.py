def sanitize_phone_number(phone):
    """Sanitize and format a phone number.

    Args:
        phone (str): The input phone number to sanitize.

    Returns:
        str: The sanitized and formatted phone number.
    """
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone
