import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: object) -> object:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        else:
            return NotImplemented

    def __sub__(self, other: object) -> object:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        else:
            return NotImplemented

    def __mul__(self, other: float) -> object:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> object:
        divide = math.sqrt((self.x ** 2) + (self.y ** 2))
        return Vector(self.x / divide, self.y / divide)

    def angle_between(self, other: "Vector") -> float:
        first = self.x * other.x + self.y * other.y
        second = (math.sqrt((self.x ** 2) + (self.y ** 2)) * math.sqrt(
            (other.x ** 2) + (other.y ** 2)))
        result = math.degrees(math.acos(first / second))
        return round(result)

    def get_angle(self) -> float:
        first = self.x * 0 + self.y * 1
        second = (math.sqrt((self.x ** 2) + (self.y ** 2)) * math.sqrt(
            (0 ** 2) + (1 ** 2)))
        result = math.degrees(math.acos(first / second))
        return round(result)

    def rotate(self, angle: int) -> object:
        rad = math.radians(angle)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)

        coordinate_x = self.x * cos_a - self.y * sin_a
        coordinate_y = self.x * sin_a + self.y * cos_a
        return Vector(coordinate_x, coordinate_y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> object:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])
