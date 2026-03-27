class Notifier:
    """Базовый класс для всех уведомлений"""
    
    def send(self, message: str) -> str:
        """Отправка сообщения"""
        return f"Отправка сообщения: {message}"


class EmailNotifier(Notifier):
    """Уведомление по email"""
    
    def __init__(self, email_address: str):
        self.email_address = email_address
    
    def send(self, message: str) -> str:
        """Отправка email-сообщения"""
        return f"📧 EMAIL на {self.email_address}: {message}"


class SMSNotifier(Notifier):
    """Уведомление по SMS"""
    
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
    
    def send(self, message: str) -> str:
        """Отправка SMS-сообщения"""
        return f" SMS на {self.phone_number}: {message}"


class PushNotifier(Notifier):
    """Push-уведомление"""
    
    def __init__(self, device_token: str):
        self.device_token = device_token
    
    def send(self, message: str) -> str:
        """Отправка push-уведомления"""
        return f" PUSH на устройство (токен: {self.device_token[:8]}...): {message}"


def notify_all(notifiers: list, message: str):
    """
    Полиморфная функция для отправки сообщения через все способы уведомления
    
    Args:
        notifiers: список объектов-уведомителей
        message: сообщение для отправки
    """
    print("\n" + "=" * 50)
    print(f"РАССЫЛКА СООБЩЕНИЯ: \"{message}\"")
    print("=" * 50)
    
    for notifier in notifiers:
        if isinstance(notifier, Notifier):
            result = notifier.send(message)
            print(result)
        else:
            print(f"Ошибка: {notifier} не является уведомителем")


# Демонстрация работы системы уведомлений
print("СИСТЕМА УВЕДОМЛЕНИЙ")
print("=" * 50)

# Создаём различные способы уведомлений
notifiers = [
    EmailNotifier("user@example.com"),
    SMSNotifier("+7 (999) 123-45-67"),
    PushNotifier("device_token_abc123xyz789"),
    EmailNotifier("admin@company.ru"),
    SMSNotifier("+7 (888) 765-43-21")
]

# Отправляем первое сообщение
notify_all(notifiers, "Важное обновление системы!")

# Отправляем второе сообщение
notify_all(notifiers, "Напоминание: встреча в 15:00")

# Добавляем новый способ уведомления
print("\n" + "=" * 50)
print("ДОБАВЛЯЕМ НОВЫЙ СПОСОБ УВЕДОМЛЕНИЯ")
print("=" * 50)

notifiers.append(PushNotifier("new_device_token_456"))
notify_all(notifiers, "Добро пожаловать в систему!")