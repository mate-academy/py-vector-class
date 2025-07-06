import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"Unsupported operand type(s) for +: 'Vector' "
                            f"and {type(other).__name__}")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(f"Unsupported operand type(s) for -: 'Vector' "
                            f"and {type(other).__name__}")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | int | float") -> "Vector | float":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Vector' "
                            f"and {type(other).__name__}")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0], end_point[1]
                   - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        len = self.get_length()
        if len == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / len, self.y / len)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot compute angle with zero-length vector")
        cos_a = dot_product / (len_self * len_other)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_axis_vector = Vector(0, 1)
        dot_product = self * y_axis_vector
        len_self = self.get_length()
        len_y_axis = 1
        if len_self == 0:
            raise ValueError("Cannot compute angle for zero-length vector")
        cos_a = dot_product / (len_self * len_y_axis)
        angle = math.acos(cos_a)
        return int(round(math.degrees(angle)))

    def rotate(self, degrees: int) -> "Vector":
        len_self = self.get_length()
        if len_self == 0:
            raise ValueError("Cannot rotate zero-length vector")
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(round(new_x, 2), round(new_y, 2))
