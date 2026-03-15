
# Virkņu funkcijas


def capitalize(text):
    """
    Pārvērš pirmo burtu lielajā.

    Args:
        text (str): ievades teksts

    Returns:
        str: teksts ar lielo pirmo burtu

    Example:
        >>> capitalize("hello")
        'Hello'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        return ""

    return text[0].upper() + text[1:]


def truncate(text, max_len=20):
    """
    Saīsina tekstu līdz norādītajam garumam un pievieno "...".

    Args:
        text (str): ievades teksts
        max_len (int): maksimālais garums

    Returns:
        str: saīsinātais teksts

    Example:
        >>> truncate("This is a long sentence", 10)
        'This is a ...'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if max_len < 0:
        raise ValueError("max_len must be >= 0")

    if len(text) <= max_len:
        return text

    return text[:max_len] + "..."


def count_words(text):
    """
    Saskaita vārdus tekstā.

    Args:
        text (str): ievades teksts

    Returns:
        int: vārdu skaits

    Example:
        >>> count_words("Hello world")
        2
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = text.split()
    return len(words)



# Skaitļu funkcijas


def clamp(num, low, high):
    """
    Ierobežo skaitli norādītajā diapazonā.

    Args:
        num (int|float): skaitlis
        low (int|float): minimālā robeža
        high (int|float): maksimālā robeža

    Returns:
        int|float: ierobežotā vērtība

    Example:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
    """
    if low > high:
        raise ValueError("low cannot be greater than high")

    return max(low, min(num, high))


def is_prime(num):
    """
    Pārbauda vai skaitlis ir pirmskaitlis.

    Args:
        num (int): skaitlis

    Returns:
        bool: True ja pirmskaitlis, False citādi

    Example:
        >>> is_prime(7)
        True
    """
    if not isinstance(num, int):
        raise TypeError("num must be an integer")

    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def factorial(n):
    """
    Aprēķina n! (faktoriālu).

    Args:
        n (int): skaitlis >= 0

    Returns:
        int: faktoriāls

    Example:
        >>> factorial(5)
        120
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result



# Sarakstu funkcijas


def total(numbers):
    """
    Aprēķina saraksta summu.

    Args:
        numbers (list): skaitļu saraksts

    Returns:
        int|float: summa

    Example:
        >>> total([1,2,3])
        6
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")

    s = 0
    for n in numbers:
        s += n

    return s


def average(numbers):
    """
    Aprēķina saraksta vidējo vērtību.

    Args:
        numbers (list): skaitļu saraksts

    Returns:
        float: vidējā vērtība

    Example:
        >>> average([2,4,6])
        4.0
    """
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")

    if len(numbers) == 0:
        raise ValueError("numbers list cannot be empty")

    s = total(numbers)

    count = 0
    for _ in numbers:
        count += 1

    return s / count


# Demonstrācija


if __name__ == "__main__":

    print(capitalize("hello"))
    print(truncate("This is a very long sentence", 15))
    print(count_words("Python makes programming fun"))

    print(clamp(15, 0, 10))
    print(is_prime(13))
    print(factorial(5))

    nums = [2, 4, 6, 8]
    print(total(nums))
    print(average(nums))