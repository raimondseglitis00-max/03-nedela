# E-pasta validācija


def is_email(text):
    """
    Pārbauda vai teksts ir vienkāršs e-pasta formāts.

    Args:
        text (str): ievades teksts

    Returns:
        bool: True ja izskatās pēc e-pasta, False citādi

    Example:
        >>> is_email("anna@inbox.lv")
        True
        >>> is_email("anna")
        False
    """
    if not isinstance(text, str):
        return False

    if "@" not in text or "." not in text:
        return False

    parts = text.split("@")

    if len(parts) != 2:
        return False

    if parts[0] == "" or parts[1] == "":
        return False

    if "." not in parts[1]:
        return False

    return True



# Telefona numurs


def is_phone_number(text):
    """
    Pārbauda vai teksts ir Latvijas telefona numurs formātā +371 XXXXXXXX.

    Args:
        text (str): telefona numurs

    Returns:
        bool: True ja formāts ir pareizs

    Example:
        >>> is_phone_number("+371 26123456")
        True
    """
    if not isinstance(text, str):
        return False

    if not text.startswith("+371 "):
        return False

    number = text[5:]

    if len(number) != 8:
        return False

    if not number.isdigit():
        return False

    return True



# Vecuma validācija


def is_valid_age(age):
    """
    Pārbauda vai vecums ir vesels skaitlis diapazonā 0–150.

    Args:
        age (int): vecums

    Returns:
        bool: True ja vecums ir derīgs

    Example:
        >>> is_valid_age(25)
        True
    """
    if not isinstance(age, int):
        return False

    return 0 <= age <= 150



# Paroles stiprums


def is_strong_password(text):
    """
    Pārbauda vai parole ir pietiekami stipra.

    Nosacījumi:
    - vismaz 8 simboli
    - satur vismaz vienu burtu
    - satur vismaz vienu ciparu

    Args:
        text (str): parole

    Returns:
        bool: True ja parole ir stipra

    Example:
        >>> is_strong_password("abc12345")
        True
    """
    if not isinstance(text, str):
        return False

    if len(text) < 8:
        return False

    has_letter = False
    has_digit = False

    for ch in text:
        if ch.isalpha():
            has_letter = True
        if ch.isdigit():
            has_digit = True

    return has_letter and has_digit



# Datuma validācija


def is_valid_date(text):
    """
    Pārbauda vai teksts ir datums formātā YYYY-MM-DD.

    Pārbauda tikai pamata struktūru.

    Args:
        text (str): datums

    Returns:
        bool: True ja formāts derīgs

    Example:
        >>> is_valid_date("2024-05-10")
        True
    """
    if not isinstance(text, str):
        return False

    parts = text.split("-")

    if len(parts) != 3:
        return False

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return False

    month = int(month)
    day = int(day)

    if not (1 <= month <= 12):
        return False

    if not (1 <= day <= 31):
        return False

    return True



# Testi


if __name__ == "__main__":

    print("EMAIL TESTI")
    print(is_email("anna@inbox.lv"))   # True
    print(is_email("anna"))            # False
    print(is_email("anna@"))           # False

    print("\nPHONE TESTI")
    print(is_phone_number("+371 26123456"))  # True
    print(is_phone_number("26123456"))       # False
    print(is_phone_number("+371 123"))       # False

    print("\nAGE TESTI")
    print(is_valid_age(25))    # True
    print(is_valid_age(-5))    # False
    print(is_valid_age(200))   # False

    print("\nPASSWORD TESTI")
    print(is_strong_password("abc12345"))  # True
    print(is_strong_password("abcdefg"))   # False
    print(is_strong_password("12345678"))  # False

    print("\nDATE TESTI")
    print(is_valid_date("2024-05-10"))  # True
    print(is_valid_date("2024-13-01"))  # False
    print(is_valid_date("10-05-2024"))  # False