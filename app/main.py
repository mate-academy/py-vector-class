import math

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Unsupported type for addition")

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Unsupported type for subtraction")

    def __mul__(self, other: "Vector | float") -> "Vector | float":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError("Unsupported type for multiplication")

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        if isinstance(other, Vector):
            cos_a = ((self.x * other.x + self.y * other.y)
                     / (self.get_length() * other.get_length()))
            angle = math.degrees(math.acos(cos_a))
            return round(angle)
        raise TypeError("Unsupported type for angle calculation")

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.y, self.x))
        if angle < 0:
            angle += 360
        return round(angle)

    def rotate(self, degrees: int) -> "Vector":
        angle = math.radians(degrees)
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)
        return Vector(self.x * cos_angle - self.y * sin_angle,
                      self.x * sin_angle + self.y * cos_angle)
