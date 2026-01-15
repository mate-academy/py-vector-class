import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    @property
    def x(self) -> float:
        return self.coord_x

    @property
    def y(self) -> float:
        return self.coord_y

    def __add__(self, other: "Vector") -> "Vector":
        return (Vector
                (self.coord_x + other.coord_x, self.coord_y + other.coord_y))

    def __sub__(self, other: "Vector") -> "Vector":
        return (Vector
                (self.coord_x - other.coord_x, self.coord_y - other.coord_y))

    def __mul__(self, other: float) -> float:
        if isinstance(other, (int, float)):
            return Vector(self.coord_x * other, self.coord_y * other)
        elif isinstance(other, Vector):
            return self.coord_x * other.coord_x + self.coord_y * other.coord_y
        raise TypeError(
            "Unsupported operand type for *: 'Vector' and '{}'".format(
                type(other)
            )
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.coord_x ** 2 + self.coord_y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize the zero vector")
        return Vector(self.coord_x / length, self.coord_y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_angle = dot_product / lengths_product
        angle_in_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_in_degrees)

    def get_angle(self) -> int:
        return abs(int(math.degrees(math.atan2(self.coord_x, self.coord_y))))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.coord_x * cos_theta - self.coord_y * sin_theta
        new_y = self.coord_x * sin_theta + self.coord_y * cos_theta
        return Vector(new_x, new_y)
# check
