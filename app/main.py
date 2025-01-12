from __future__ import annotations
class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector_1: Vector, vector_2: Vector):
        return Vector(vector_1.x + vector_2.x, vector_1.y + vector_2.y)

    def __sub__(self, vector_1: Vector, vector_2: Vector):
        return Vector(vector_1.x - vector_2.x, vector_1.y - vector_2.y)

    def __mul__(self,  vector_1: Vector, vector_2: Vector)):
        #a · b = |a| × |b| × cos(angle)
        v1_l = self.get_length(vector_1)
        v2_l = self.get_length(vector_2)
        angle = angle_between(vector_1, vector_2)
        return v1_l * v2_l * math.cos(angle)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point : tuple) -> Vector:
        return cls(start_point[0] - end_point[0], start_point[1] - end_point[1])

    def get_length(self, vector: Vector) -> float:
        return pow((pow(vector.x, 2) + pow(vector.y, 2)), 1 / 2)

    def get_normalized(self):
        pass

    def angle_between(self, vector_1: Vector, vector_2: Vector):
        return vector_1.x * vector_2.x + vector_1.y * vector_2.y

    def rotate(self):
        pass
