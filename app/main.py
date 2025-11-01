from __future__ import annotations

class Vector:
    def __init__(self, x: float | int, y: float | int):
        x, y = round(x, 2), round(y, 2)
        self.x = x
        self.y = y


    def __add__(self, other) -> Vector:
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return Vector(sum_x, sum_y)

    def __sub__(self, other) -> Vector:
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return Vector(sub_x, sub_y)

    def __mul__(self, num: int | float | Vector) -> Vector:
        if isinstance(num, Vector):
            mul_x = self.x * num.x
            mul_y = self.y * num.y
            dot_product = mul_x + mul_y
            return dot_product

        mul_x = self.x * num
        mul_y = self.y * num
        return Vector(mul_x, mul_y)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        sub_x = end_point[0] - start_point[0]
        sub_y = end_point[1] - start_point[1]
        return cls(sub_x, sub_y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        norma = self.get_length()
        return Vector(self.x / norma, self.y / norma)

