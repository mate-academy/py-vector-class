import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)


    def __add__(self, other):
        return Vector(
            x=round(self.x + other.x, 2),
            y=round(self.y + other.y, 2)
        )

    def __sub__(self, other):
        return Vector(
            x=round(self.x - other.x, 2),
            y=round(self.y - other.y, 2)
        )

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector(
                x=round(self.x * other, 2),
                y=round(self.y * other, 2)
            )
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length()
        )

    def angle_between(self, vector: Vector):
        scalar = (self.x * vector.x) + (self.y * vector.y)
        sub_length = self.get_length() * vector.get_length()
        return round(math.degrees(math.acos(scalar / sub_length)))

    def get_angle(self) -> float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: float):
        rad = math.radians(degrees)
        return Vector(
            x=round((self.x * math.cos(rad)) - (self.y * math.sin(rad)), 2),
            y=round((self.x * math.sin(rad)) + (self.y * math.cos(rad)), 2)
        )
