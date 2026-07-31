import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __repr__(self) -> str:
        return f"Vector {self.x}, {self.y}"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: float) -> float:
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return round(length, 15)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        normalized_x = round(self.x / length, 2)
        normalized_y = round(self.y / length, 2)
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        cos_a = max(-1.0, min(1.0, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        if self.x == 0 and self.y == 0:
            return 0
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        angle_deg = (- angle_deg + 360) % 360
        return round(angle_deg)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(
            radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(
            radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
