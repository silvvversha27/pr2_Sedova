# Вариант 9
# Задание 11.1
class Rectangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_square(self):
        # Проверяем, является ли прямоугольник квадратом
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        return width == height

    def draw_on_image(self, image):
        # Изображаем прямоугольник на форме, закрашенный зеленым цветом
        # (Здесь предполагается, что есть способ рисования на форме, например, с использованием библиотеки PIL)
        pass

    def __str__(self):
        # Формируем строку информации об объекте
        return f"Прямоугольник: x1={self.x1}, y1={self.y1}, x2={self.x2}, y2={self.y2}"

# Пример использования
print("Задание №1:")
print("Например координаты:(0, 0, 5, 5)")
# Пользовательский ввод координат
x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

# Создаем объект прямоугольника на основе пользовательского ввода
rect = Rectangle(x1, y1, x2, y2)
print(rect)
if rect.is_square():
    print("Прямоугольник является квадратом.")
else:
    print("Прямоугольник не является квадратом.")

# Задание 11.2
class ColoredRectangle(Rectangle):
    def __init__(self, x1=0, y1=0, x2=0, y2=0, text="", color=""):
        # Вызываем конструктор класса-родителя Rectangle
        super().__init__(x1, y1, x2, y2)
        self.text = text
        self.color = color

    def calculate_properties(self):
        # Функция обработки данных: произведение периметра и длины диагонали в пикселях
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)
        perimeter = 2 * (width + height)
        diagonal_length = (width ** 2 + height ** 2) ** 0.5
        return perimeter, diagonal_length

    def __str__(self):
        # Формируем строку информации об объекте
        info = super().__str__()
        return f"{info}, Текст: {self.text}, Цвет: {self.color}"

print("Задание №2:")
# Пользовательский ввод данных
x1 = int(input("Введите x1 (координата X левого верхнего угла): "))
y1 = int(input("Введите y1 (координата Y левого верхнего угла): "))
x2 = int(input("Введите x2 (координата X правого нижнего угла): "))
y2 = int(input("Введите y2 (координата Y правого нижнего угла): "))
text = input("Введите текст, который будет на изображении: ")
color = input("Введите цвет закрашивания прямоугольника: ")

# Создаем объект класса-потомка ColoredRectangle без поля image
colored_rect = ColoredRectangle(x1, y1, x2, y2, text, color)
print(colored_rect)

# Вызываем функцию обработки данных и выводим результат
perimeter, diagonal_length = colored_rect.calculate_properties()
print(f"Периметр прямоугольника: {perimeter} пикселей")
print(f"Длина диагонали прямоугольника: {diagonal_length} пикселей")

# Задание 11.3
class Movie:
    def __init__(self, title, director, duration_minutes, num_actors):
        self.title = title
        self.director = director
        self.duration_minutes = duration_minutes
        self.num_actors = num_actors

    def cost(self):
        base_cost = self.duration_minutes * 20 + self.num_actors * 30
        if self.director == "Стивен Спилберг" or self.director == "Джеймс Кэмерон":
            return base_cost * 2
        else:
            return base_cost

    def info(self):
        return f"Фильм: {self.title}, Режиссер: {self.director}, Длительность: {self.duration_minutes} минут, " \
               f"Количество актеров: {self.num_actors}, Стоимость: {self.cost()} тыс. $"


class Cartoon(Movie):
    def cost(self):
        return self.duration_minutes * 25 + self.num_actors * 10


# Создаем объекты фильмов и мультфильма
movie1 = Movie("Фильм 1", "Стивен Спилберг", 120, 5)
movie2 = Movie("Фильм 2", "Ежи Гофман", 90, 4)
cartoon = Cartoon("Мультфильм 1", "Другой Режиссер", 60, 2)

# Выводим информацию о фильмах и мультфильме
print("Задание №3:")
print(movie1.info())
print(movie2.info())
print(cartoon.info())