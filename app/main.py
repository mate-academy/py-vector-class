import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: "Vector") -> "Vector":
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: "Vector | float") -> "Vector | float":
        if isinstance(other, Vector):
            new_x = self.x * other.x
            new_y = self.y * other.y
            return new_x + new_y
        elif isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> "Vector":
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        check_length = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        return check_length

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot = self * other
        lengths = self.get_length() * other.get_length()
        if lengths == 0:
            return 0
        cos_a = dot / lengths
        cos_a = max(min(cos_a, 1), -1)
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
