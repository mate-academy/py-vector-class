import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("Can only add another Vector")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract another Vector")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self,
                other: "Vector" or float or int)\
            -> "Vector" or float or int:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # Dot product
        else:
            raise TypeError("Can only multiply by a number or another Vector")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 +
                         self.y**2)  # Corrected: self.x2 and self.y2

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)  # Handle zero-length vector
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other_vector: "Vector") -> int:
        dot_product = self.x * other_vector.x + self.y * other_vector.y
        magnitude_product = self.get_length() * other_vector.get_length()

        if magnitude_product == 0:
            return 0  # Handle zero-length vector

        cos_a = dot_product / magnitude_product
        angle_rad = math.acos(cos_a)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(round(new_x, 2), round(new_y, 2))
