class Employee:
    """Базовый класс для всех сотрудников"""
    
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
    
    def work(self) -> str:
        """Базовый метод работы"""
        return f"{self.name} выполняет общие рабочие обязанности"
    
    def get_info(self) -> str:
        """Возвращает основную информацию о сотруднике"""
        return f"Имя: {self.name}, Зарплата: {self.salary} руб."


class Developer(Employee):
    """Класс разработчика"""
    
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def write_code(self) -> str:
        """Написание кода"""
        return f"{self.name} пишет код на {self.programming_language}"
    
    def work(self) -> str:
        """Переопределённый метод работы"""
        return self.write_code()
    
    def get_info(self) -> str:
        """Расширенный метод получения информации"""
        base_info = super().get_info()
        return f"{base_info}, Язык программирования: {self.programming_language}"


class Designer(Employee):
    """Класс дизайнера"""
    
    def __init__(self, name: str, salary: float, software: str):
        super().__init__(name, salary)
        self.software = software
    
    def design(self) -> str:
        """Создание дизайна"""
        return f"{self.name} создаёт дизайн в {self.software}"
    
    def work(self) -> str:
        """Переопределённый метод работы"""
        return self.design()
    
    def get_info(self) -> str:
        """Расширенный метод получения информации"""
        base_info = super().get_info()
        return f"{base_info}, Программа: {self.software}"


class Manager(Employee):
    """Класс менеджера"""
    
    def __init__(self, name: str, salary: float, team_size: int):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def manage(self) -> str:
        """Управление командой"""
        return f"{self.name} управляет командой из {self.team_size} человек"
    
    def work(self) -> str:
        """Переопределённый метод работы"""
        return self.manage()
    
    def get_info(self) -> str:
        """Расширенный метод получения информации"""
        base_info = super().get_info()
        return f"{base_info}, Размер команды: {self.team_size}"


# Создание списка сотрудников и демонстрация работы
employees = [
    Developer("Анна Смирнова", 120000, "Python"),
    Designer("Иван Петров", 90000, "Figma"),
    Manager("Елена Козлова", 150000, 5),
    Developer("Максим Иванов", 130000, "JavaScript"),
    Designer("Ольга Сидорова", 85000, "Adobe Photoshop")
]

print("=" * 50)
print("ИНФОРМАЦИЯ О СОТРУДНИКАХ")
print("=" * 50)

for employee in employees:
    print(employee.get_info())
    print(f"Работа: {employee.work()}")
    print("-" * 50)
