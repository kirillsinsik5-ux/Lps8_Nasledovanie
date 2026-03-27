class Animal:
    """Базовый класс для всех животных"""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def make_sound(self) -> str:
        """Издание звука"""
        return f"{self.name} издаёт звук"
    
    def move(self) -> str:
        """Способ передвижения"""
        return f"{self.name} двигается"


class Mammal(Animal):
    """Класс млекопитающих"""
    
    def __init__(self, name: str, age: int, hair_color: str):
        super().__init__(name, age)
        self.hair_color = hair_color
    
    def feed_milk(self) -> str:
        """Кормление молоком"""
        return f"{self.name} кормит детёнышей молоком"
    
    def make_sound(self) -> str:
        """Переопределённый метод издания звука"""
        return f"{self.name} рычит/мяукает"
    
    def move(self) -> str:
        """Переопределённый метод передвижения"""
        return f"{self.name} бегает на четырёх лапах"


class Bird(Animal):
    """Класс птиц"""
    
    def __init__(self, name: str, age: int, wing_span: float):
        super().__init__(name, age)
        self.wing_span = wing_span
    
    def fly(self) -> str:
        """Полёт"""
        return f"{self.name} летает с размахом крыльев {self.wing_span} м"
    
    def make_sound(self) -> str:
        """Переопределённый метод издания звука"""
        return f"{self.name} чирикает/каркает"
    
    def move(self) -> str:
        """Переопределённый метод передвижения"""
        return f"{self.name} летает по воздуху"


class Fish(Animal):
    """Класс рыб"""
    
    def __init__(self, name: str, age: int, water_type: str):
        super().__init__(name, age)
        self.water_type = water_type
    
    def swim(self) -> str:
        """Плавание"""
        return f"{self.name} плавает в {self.water_type} воде"
    
    def make_sound(self) -> str:
        """Переопределённый метод издания звука"""
        return f"{self.name} издает булькающие звуки"
    
    def move(self) -> str:
        """Переопределённый метод передвижения"""
        return f"{self.name} плавает с помощью плавников"


# Демонстрация полиморфизма
print("=" * 50)
print("ПОЛИМОРФИЗМ ЖИВОТНЫХ")
print("=" * 50)

animals = [
    Mammal("Лев", 5, "золотистый"),
    Bird("Орёл", 3, 2.5),
    Fish("Золотая рыбка", 1, "пресной"),
    Mammal("Кошка", 2, "белый"),
    Bird("Воробей", 1, 0.2),
    Fish("Акула", 7, "солёной")
]

print("\n--- ЗВУКИ ЖИВОТНЫХ ---")
for animal in animals:
    print(animal.make_sound())

print("\n--- СПОСОБЫ ПЕРЕДВИЖЕНИЯ ---")
for animal in animals:
    print(animal.move())

print("\n--- ДОПОЛНИТЕЛЬНЫЕ ВОЗМОЖНОСТИ ---")
for animal in animals:
    if isinstance(animal, Mammal):
        print(animal.feed_milk())
    elif isinstance(animal, Bird):
        print(animal.fly())
    elif isinstance(animal, Fish):
        print(animal.swim())