import math


class Vector:
    # write your code here
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: float) -> float:
        return Vector(
            self.x_coord + other.x_coord, self.y_coord + other.y_coord
        )

    def __sub__(self, other: float) -> float:
        return Vector(
            self.x_coord - other.x_coord, self.y_coord - other.y_coord
        )

    def __mul__(self, other: float) -> float:
        if isinstance(other, Vector):
            return self.x_coord * other.x_coord + self.y_coord * other.y_coord
        else:
            return Vector(self.x_coord * other, self.y_coord * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: float, end_point: float
    ) -> float:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x_coord**2 + self.y_coord**2)

    def get_normalized(self) -> float:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x_coord / length, self.y_coord / length)

    def angle_between(self, other: float) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = self.y_coord / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> float:
        radians = math.radians(degrees)
        new_x = \
            self.x_coord * math.cos(radians) - self.y_coord * math.sin(radians)
        new_y = \
            self.x_coord * math.sin(radians) + self.y_coord * math.cos(radians)
        return Vector(new_x, new_y)
