#Методы класса и статические методы (79–85)
#1
class Pizza:
    def __init__(self, name, ingredients, size=30):
        self.name = name
        self.ingredients = ingredients
        self.size = size

    @classmethod
    def margherita(cls):
        return cls("Маргарита", ["томатный соус", "моцарелла", "базилик"])

    def __repr__(self):
        return f"Pizza({self.name}, {self.ingredients}, {self.size} см)"


p1 = Pizza("Пепперони", ["томатный соус", "моцарелла", "пепперони"], 35)
p2 = Pizza.margherita()
print(p1)
print(p2)
#2
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(Date.is_leap_year(2024))  #труе
print(Date.is_leap_year(1900))  #фалсе
print(Date.is_leap_year(2000))  #труе
#vисокосный год: делится на 4, но не на 100, кроме случаев, когда делится на 400.

#3
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data_string):
        name, salary = data_string.split(",")
        return cls(name.strip(), int(salary))

    def __repr__(self):
        return f"Employee({self.name}, {self.salary})"


emp = Employee.from_string("Иван,50000")
print(emp.name)
print(emp.salary)

#4
class Circle:
    def __init__(self, radius):
        Circle.validate_radius(radius)
        self.radius = radius

    @staticmethod
    def validate_radius(radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        return True


c = Circle(5)
print(c.radius)  # 5

try:
    bad = Circle(-3)
except ValueError as e:
    print(e)

#5
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9


print(TemperatureConverter.celsius_to_fahrenheit(100))
print(TemperatureConverter.fahrenheit_to_celsius(32))

#6
class Student:
    school_name = "Школа №1"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name


s1 = Student("Аня")
s2 = Student("Борис")
print(s1.school_name, s2.school_name)

Student.change_school("Гимназия №5")
print(s1.school_name, s2.school_name)

#7
class Burger:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    @classmethod
    def cheeseburger(cls):
        return cls("Чизбургер", ["булочка", "котлета", "сыр", "соус"])

    @classmethod
    def veggie_burger(cls):
        return cls("Вегетарианский бургер",
                   ["булочка", "овощная котлета", "салат", "помидор"])

    @classmethod
    def double_burger(cls):
        return cls("Двойной бургер",
                   ["булочка", "котлета", "котлета", "сыр", "соус"])

    def __repr__(self):
        return f"{self.name}: {', '.join(self.ingredients)}"


print(Burger.cheeseburger())
print(Burger.veggie_burger())
print(Burger.double_burger())