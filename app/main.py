import math


class Vector:
    # flake8: noqa N815
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)  # noqa: N815
        self.y = round(y, 2)  # noqa: N815

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError("Type not supported")

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        lenght = self.get_length()
        if lenght == 0:
            raise ZeroDivisionError("Cannot calculate length")
        return Vector(round(self.x / lenght, 2), round(self.y / lenght, 2))

    def angle_between(self, other: Vector) -> int:
        dot = (self.x * other.x) + (self.y * other.y)
        magnitude_v1 = math.sqrt(self.x**2 + self.y**2)
        magnitude_v2 = math.sqrt(other.x**2 + other.y**2)
        if magnitude_v1 != 0 and magnitude_v2 != 0:
            cos = dot / (magnitude_v1 * magnitude_v2)
            angle_rad = math.acos(cos)
            return round(math.degrees(angle_rad))
        raise ZeroDivisionError("Cannot calculate angle")

    def get_angle(self) -> float:
        angle = math.degrees(math.atan2(self.x, self.y))
        if angle < 0:
            angle += 360
        if angle > 180:
            angle = 360 - angle
        return round(angle)

    def rotate(self, angle: float) -> Vector:
        radians = math.radians(angle)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
