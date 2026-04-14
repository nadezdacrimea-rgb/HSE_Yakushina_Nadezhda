# -*- coding: utf-8 -*-

def clean_inn_string(inn_str: str) -> str:
    """Удаляет из строки все символы, кроме цифр (пробелы, дефисы и т.п.)."""
    return ''.join(ch for ch in inn_str if ch.isdigit())

def compute_checksum(digits: list, weights: list) -> int:
    """
    Вычисляет контрольное число по алгоритму:
    сумма произведений цифр на весовые коэффициенты, затем остаток от деления на 11,
    если результат > 9, берётся остаток от деления на 10.
    """
    if len(digits) != len(weights):
        raise ValueError("Длина списка цифр не совпадает с длиной весовых коэффициентов")
    total = sum(d * w for d, w in zip(digits, weights))
    checksum = total % 11
    if checksum > 9:
        checksum %= 10
    return checksum

def validate_inn_10(digits: list) -> bool:
    """
    Валидация 10-значного ИНН (организации).
    digits: список из 10 целых цифр.
    """
    # Весовые коэффициенты для первых 9 цифр
    weights = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    # Вычисляем контрольное число для первых 9 цифр
    calculated = compute_checksum(digits[:9], weights)
    # Сравниваем с 10-й цифрой
    return calculated == digits[9]

def validate_inn_12(digits: list) -> bool:
    """
    Валидация 12-значного ИНН (физического лица или ИП).
    digits: список из 12 целых цифр.
    """
    # Первое контрольное число (для первых 10 цифр)
    weights1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    check1 = compute_checksum(digits[:10], weights1)
    if check1 != digits[10]:
        return False

    # Второе контрольное число (для первых 11 цифр)
    weights2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    check2 = compute_checksum(digits[:11], weights2)
    return check2 == digits[11]

def is_valid_inn(inn_str: str) -> bool:
    """
    Основная функция валидации ИНН.
    Принимает строку (возможно с пробелами/дефисами) и возвращает True/False.
    """
    inn_clean = clean_inn_string(inn_str)
    
    # Проверка: строка должна состоять только из цифр
    if not inn_clean.isdigit():
        return False
    
    digits = [int(ch) for ch in inn_clean]
    length = len(digits)
    
    if length == 10:
        return validate_inn_10(digits)
    elif length == 12:
        return validate_inn_12(digits)
    else:
        return False  # неверная длина

# ==================== ПРИМЕРЫ ТЕСТИРОВАНИЯ ====================
if __name__ == "__main__":
    # Корректные ИНН (примеры найдены в открытых источниках)
    test_inns = [
        "7707083893",          # 10 знаков (Сбербанк) – проверьте реальный, здесь демо
        "7728168971",          # другой пример
        "500100732259",        # 12 знаков (физлицо)
        "123456789047",        # пример с корректными контрольными числами (подобран)
    ]
    
    # Некорректные
    invalid_inns = [
        "7707083894",          # неверное контрольное число
        "1234567890",          # 10 знаков, но неправильно
        "500100732250",        # 12 знаков, неверные контроли
        "123",                 # слишком короткий
        "12a45b7890",          # содержит буквы
    ]
    
    print("=== Проверка корректных ИНН ===")
    for inn in test_inns:
        print(f"{inn}: {is_valid_inn(inn)}")
    
    print("\n=== Проверка некорректных ИНН ===")
    for inn in invalid_inns:
        print(f"{inn}: {is_valid_inn(inn)}")