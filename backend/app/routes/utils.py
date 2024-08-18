import random
import string
import re

def generate_url() -> str:
    """
    функция для создания уникальных строк
    """
    characters = string.ascii_letters  # Все буквы (верхний и нижний регистр)
    url = ''.join(random.choice(characters) for _ in range(6))
    return url


def validate_url(url: str) -> bool:
    """
    Валидация url ссылок
    """
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://' # http:// или https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|[0-9.]+|' # доменное имя
        r'\[?[A-F0-9:*]+\]?)' # или ipv4/ipv6
        r'(?::\d+)?' # порт (необязательный)
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(url_pattern, url) is not None
