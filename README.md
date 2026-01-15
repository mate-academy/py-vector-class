# Класс Vector

Прочитайте [руководство](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) перед началом.

Для получения информации о векторах используйте следующие материалы:
- [Векторы на координатной плоскости](https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_(OpenStax)/Book%3A_University_Physics_I_-_Mechanics_Sound_Oscillations_and_Waves_(OpenStax)/02%3A_Vectors/2.04%3A__Coordinate_Systems_and_Components_of_a_Vector_(Part_1))
- [Вектор по двум точкам](https://www.varsitytutors.com/precalculus-help/find-a-direction-vector-when-given-two-points)
- [Сложение векторов](https://www.dummies.com/article/academics-the-arts/science/physics/how-to-add-vectors-together-148601)
- [Нормализованный вектор](https://mathworld.wolfram.com/NormalizedVector.html)
- [Скалярное произведение векторов](https://www.mathsisfun.com/algebra/vectors-dot-product.html)
- [Угол между двумя векторами](https://www.wikihow.com/Find-the-Angle-Between-Two-Vectors)
- [Поворот векторов](https://matthew-brett.github.io/teaching/rotation_2d.html)

Вы недавно получили работу в компании по разработке игр на должность графического инженера. Вам нужно рассчитывать трассировку света, но это невозможно без использования векторов.

Вектор на координатной плоскости — это направленный отрезок, который всегда начинается в точке (0, 0) и заканчивается в координатах (x, y).

Реализуйте класс Vector, его метод `__init__` принимает и сохраняет две координаты: x, y — координаты конца вектора, **округленные до двух знаков после запятой**.

Класс Vector должен иметь следующие магические методы:
- `__add__` — сложение двух векторов должно возвращать Vector.
- `__sub__` — вычитание двух векторов должно возвращать Vector.
- `__mul__` — умножение вектора на число должно возвращать другой Vector. Умножение вектора на вектор должно возвращать их скалярное произведение.

Также класс Vector должен иметь следующие методы:
- `create_vector_by_two_points` — принимает `start_point` (кортеж координат точки начала вектора) и `end_point` (кортеж координат точки конца вектора). Возвращает Vector. **Примечание**: этот метод должен быть `classmethod`.
- `get_length` — возвращает длину вектора.
- `get_normalized` — возвращает нормализованную копию вектора.
- `` angle_between— принимает `vector` и возвращает угол между текущим вектором и `vector` в целых градусах. **Примечание**: в этом методе округляйте только возвращаемые градусы.
- `` —get_angle возвращает угол между текущим вектором и положительной осью Y.
- `rotate` — принимает `degrees` (целое число градусов поворота) и возвращает повернутый Vector на `degrees`. Вы можете использовать `math.cos` и `math.sin`, но они работают с **радианами**. Для преобразования градусов в радианы используйте `math.radians`.



# class Vector

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

In order to get information about vectors follow this:
- [Vectors on coordinate plane](https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_University_Physics_(OpenStax)/Book%3A_University_Physics_I_-_Mechanics_Sound_Oscillations_and_Waves_(OpenStax)/02%3A_Vectors/2.04%3A__Coordinate_Systems_and_Components_of_a_Vector_(Part_1))
- [Vector by two points](https://www.varsitytutors.com/precalculus-help/find-a-direction-vector-when-given-two-points)
- [Adding vectors](https://www.dummies.com/article/academics-the-arts/science/physics/how-to-add-vectors-together-148601)
- [Normalized vector](https://mathworld.wolfram.com/NormalizedVector.html)
- [Vectors dot product](https://www.mathsisfun.com/algebra/vectors-dot-product.html)
- [Angle between two vectors](https://www.wikihow.com/Find-the-Angle-Between-Two-Vectors)
- [Rotating vectors](https://matthew-brett.github.io/teaching/rotation_2d.html)

You recently got a job at a game development company as a 
graphic engineer. You have to calculate light tracing, but
it is impossible without using vectors.

Vector on coordinate plane is directed line segment, that always
starts in (0, 0) and ends in coordinates (x, y).

Implement Vector class, its `__init__` method takes and stores two 
coordinates: x, y - coordinates of end of the vector, **rounded 
to two decimals**.
```python
vector = Vector(-2.343, 8.008)
vector.x == -2.34
vector.y == 8.0
```

Vector class should have such magic methods:
- `__add__`

Addition of two Vectors should return Vector.
```python
vector1 = Vector(2, 4)
vector2 = Vector(-1, 3)
vector3 = vector1 + vector2

isinstance(vector3, Vector) is True
vector3.x == 1
vector3.y == 7
```
- `__sub__`

Subtraction of two Vectors should return Vector.
```python
vector1 = Vector(2, 4)
vector2 = Vector(-1, 3)
vector3 = vector1 - vector2

isinstance(vector3, Vector) is True
vector3.x == 3
vector3.y == 1
```
- `__mul__`

Multiplying Vector on a number should return another Vector.
```python
vector1 = Vector(2, 4)
vector2 = vector1 * 3.743
isinstance(vector2, Vector) is True
vector2.x == 7.49
vector2.y == 14.97
```
Multiplying Vector on Vector should return their dot product.
```python
vector1 = Vector(2.11, 4.55)
vector2 = Vector(-3.51, 10.33)
dot_product = vector1 * vector2
dot_product == 39.5954
```

Also, Vector class should have such methods:
- `create_vector_by_two_points`
Takes `start_point` - tuple of point coordinates, start of the vector,
`end_point` - tuple of point coordinates, end of the vector. It returns
Vector.
```python
start_point = (5.2, 2.6)
end_point = (10.7, 6)

vector = Vector.create_vector_by_two_points(start_point, end_point)
isinstance(vector, Vector) is True
vector.x == 5.5
vector.y == 3.4
```
**NOTE**: `create_vector_by_two_points` should be a `classmethod`

- `get_length`

Returns length of the vector.
```python
vector = Vector(2, 4)
vector.get_length() == 4.47213595499958
```
- `get_normalized`

Returns normalized copy of vector.
```python
vector1 = Vector(13, -4)
vector1.get_length() == 13.6

vector2 = vector1.get_normalized()

vector2.x == 0.96
vector2.y == -0.29
vector2.get_length() == 1.0
```
- `angle_between`

Takes `vector` and returns angle between current vector and `vector`
in integer degrees.
```python
vector1 = Vector(13, -4)
vector2 = Vector(-6, -11)
vector1.angle_between(vector2) == 102
```
Most likely you get cosine of the angle. To correct calculate angle
use `math` library.
For your cosine `cos_a` use `math.degrees(math.acos(cos_a))` in order 
to get degrees.

**NOTE**: In this method round only returning degrees.
- `get_angle`

Returns angle between current vector and positive Y axis.
```python
vector = Vector(33, 8)
vector.get_angle() == 76
```
- `rotate`

Takes `degrees` that is integer rotation degrees.
It returns rotated Vector by `degrees`.
```python
vector = Vector(33, 8)
vector2 = vector.rotate(45)

vector2.x == 17.68
vector2.y == 28.99
```
You may use `math.cos`, `math.sin` here, but they use **radians**.
In order to convert degrees to radians use `math.radians`.

