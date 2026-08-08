import math


class Vector:
    def __init__(self, x_dot: float, y_dot: float) -> None:
        self.x = round(x_dot, 2)
        self.y = round(y_dot, 2)

    def __add__(self, other_vector: Vector) -> Vector:
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector: Vector) -> Vector:
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __mul__(self, multiply: Vector | int | float) -> Vector | float | int:
        if isinstance(multiply, Vector):
            return self.x * multiply.x + self.y * multiply.y
        return Vector(self.x * multiply, self.y * multiply)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length > 0:
            return Vector(self.x / length, self.y / length)
        return Vector(self.x, self.y)

    def angle_between(self, other_vector: Vector) -> int:
        dot_product = self * other_vector
        length1 = self.get_length()
        length2 = other_vector.get_length()
        cos_alpha = dot_product / (length1 * length2)
        angle_radians = math.acos(cos_alpha)
        return round(math.degrees(angle_radians))

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        return round(abs(math.degrees(angle_radians)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_alpha = math.cos(radians)
        sin_alpha = math.sin(radians)
        new_x = self.x * cos_alpha - self.y * sin_alpha
        new_y = self.x * sin_alpha + self.y * cos_alpha
        return Vector(new_x, new_y)
