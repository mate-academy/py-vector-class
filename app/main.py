import math


class Vector:
    def __init__(self, x: (int, float), y: (int, float)) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: ("Vector", int, float)) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return Vector(self.x + other, self.y + other)

    def __sub__(self, other: ("Vector", int, float)) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return Vector(self.x - other, self.y - other)

    def __mul__(self, other: ("Vector", int, float)) -> ("Vector", int):
        if isinstance(other, Vector):
            return self.x * other. x + self.y * other.y
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other_vector) -> int:
        dot_product = self.x * other_vector.x + self.y * other_vector.y
        cosine_angle = dot_product / (
            self.get_length() * other_vector.get_length())
        angle_in_radians = math.acos(cosine_angle)
        angle_in_degrees = math.degrees(angle_in_radians)
        return round(angle_in_degrees)

    def get_angle(self) -> int:
        angle_to_y_axis = self.angle_between(Vector(0, 1))
        return angle_to_y_axis

    def rotate(self, degrees) -> "Vector":
        radians = math.radians(degrees)
        rotated_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rotated_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(rotated_x, rotated_y)
