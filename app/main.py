import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> float:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: object) -> object:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other: object) -> object:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            return Vector((self.x * other), (self.y * other))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> object:
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: object) -> int:
        dot_product = self * other
        length1 = self.get_length()
        length2 = other.get_length()
        if length1 == 0 or length2 == 0:
            return 0
        cos_a = dot_product / (length1 * length2)
        cos_a = max(-1.0, min(1.0, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        vector_y_axis = Vector(0, 1)
        return self.angle_between(vector_y_axis)

    def rotate(self, degrees: int) -> object:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = round(self.x * cos_theta - self.y * sin_theta, 2)
        new_y = round(self.x * sin_theta + self.y * cos_theta, 2)
        return Vector(new_x, new_y)
