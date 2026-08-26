import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(float(x_value), 2)
        self.y = round(float(y_value), 2)

    def __add__(self, other: Vector) -> Vector | None:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return None

    def __sub__(self, other: Vector) -> Vector | None:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return None

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other , self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: set,
                                    end_point: set) -> Vector:

        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return abs((self.x ** 2 + self.y ** 2) ** 0.5)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        return round(math.degrees(math.acos((self * other)
                                            / (self.get_length()
                                            * other.get_length()))))

    def get_angle(self) -> float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        return Vector(self.x * math.cos(math.radians(degrees))
                      - self.y * math.sin(math.radians(degrees)),
                      self.x * math.sin(math.radians(degrees))
                      + self.y * math.cos(math.radians(degrees)))
