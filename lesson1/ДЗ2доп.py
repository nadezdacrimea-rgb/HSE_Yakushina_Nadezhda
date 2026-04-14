# -*- coding: utf-8 -*-

def input_participants(count: int = 3) -> list:
    """
    Запрашивает у пользователя данные об участниках спора.
    
    Параметры:
    count (int): количество участников для ввода (по умолчанию 3).
    
    Возвращает:
    list: список словарей с ключами 'name', 'status', 'inn'.
    """
    participants = []
    
    print("Введите данные об участниках спора:")
    for i in range(1, count + 1):
        print(f"\n--- Участник {i} ---")
        name = input("Наименование (ФИО или название организации): ").strip()
        status = input("Статус (Истец, Ответчик, Третье лицо и т.п.): ").strip()
        inn = input("ИНН (строка из 10 или 12 цифр): ").strip()
        
        participant = {
            "name": name,
            "status": status,
            "inn": inn
        }
        participants.append(participant)
    
    return participants

def main():
    # Заполняем список участниками
    participants_list = input_participants(3)
    
    # Выводим готовую структуру
    print("\n" + "="*50)
    print("Структура «Участники спора»:")
    print(participants_list)
    
    # Для красивого вывода в виде JSON-подобной структуры
    print("\nВ читаемом виде:")
    for idx, p in enumerate(participants_list, 1):
        print(f"{idx}. {p}")

if __name__ == "__main__":
    main()